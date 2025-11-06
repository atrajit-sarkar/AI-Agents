import telebot
import os
import time
import json
import asyncio
from requests.exceptions import ConnectionError
from pathlib import Path
import agent
import dotenv
from google.genai import types
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

dotenv.load_dotenv()  # Fixed: Added parentheses to call the function
# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Add your bot token here
AUTHORIZED_CHAT_IDS = ["7990300718"]  # Add authorized chat IDs here

# Debug mode - set to True to see tool calls and detailed info
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"

bot = telebot.TeleBot(BOT_TOKEN)

# Store conversation context for each user
user_contexts = {}

# Setup ADK Runner and Session Service
APP_NAME = "telegram_system_agent"
session_service = InMemorySessionService()
runner = Runner(agent=agent.system_agent, app_name=APP_NAME, session_service=session_service)


# Pre-create sessions for authorized users
def initialize_sessions():
    """Initialize sessions for authorized users."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        for chat_id in AUTHORIZED_CHAT_IDS:
            if chat_id:
                user_id = str(chat_id)
                session_id = f"session_{chat_id}"
                session = loop.run_until_complete(
                    session_service.create_session(
                        app_name=APP_NAME,
                        user_id=user_id,
                        session_id=session_id
                    )
                )
                user_contexts[int(chat_id)] = session
    finally:
        loop.close()


# Initialize sessions at startup
initialize_sessions()


def is_authorized(chat_id):
    """Check if the user is authorized to use the bot."""
    return str(chat_id) in AUTHORIZED_CHAT_IDS or not AUTHORIZED_CHAT_IDS


@bot.message_handler(commands=['start'])
def start(message):
    """Handle the /start command."""
    chat_id = message.chat.id
    
    if not is_authorized(chat_id):
        bot.reply_to(message, "⛔ You are not authorized to use this bot.")
        return
    
    welcome_message = """
🤖 *Welcome to Telegram System Agent!*

I'm an intelligent AI agent that can help you control and manage your system remotely.

*What I can do:*
📁 File & Directory Management
📝 Read, Create, Edit, Delete Files
🔄 Copy, Move, Rename Files
💻 Execute Shell Commands
🔐 Encrypt/Decrypt Files
📸 Capture Screenshots
🎥 Record Screen
📊 Get File Information
🔧 Change File Permissions

*How to use:*
Just chat with me naturally! Tell me what you want to do, and I'll handle it.

*Examples:*
• "Show me the current directory"
• "List all files in the Documents folder"
• "Create a new file called test.txt with hello world"
• "Take a screenshot"
• "Execute the command: dir"
• "Encrypt all files in the current folder"

*Quick Commands:*
/start - Show this welcome message
/help - Get help and examples
/clear - Clear conversation context
/info - Get system information

Let's get started! What would you like me to do?
"""
    
    bot.reply_to(message, welcome_message, parse_mode='Markdown')
    
    # Notify authorized users about new user
    for admin_id in AUTHORIZED_CHAT_IDS:
        if admin_id and str(chat_id) != admin_id:
            try:
                bot.send_message(
                    admin_id,
                    f"🔔 *New User Activity*\n"
                    f"Username: @{message.chat.username or 'N/A'}\n"
                    f"User ID: {chat_id}\n"
                    f"First Name: {message.chat.first_name or 'N/A'}",
                    parse_mode='Markdown'
                )
            except:
                pass


@bot.message_handler(commands=['help'])
def help_command(message):
    """Handle the /help command."""
    if not is_authorized(message.chat.id):
        bot.reply_to(message, "⛔ You are not authorized to use this bot.")
        return
    
    help_message = """
📖 *Help & Examples*

*File Operations:*
• "Show files in current directory"
• "Read the file config.txt"
• "Create a file named test.py with print('Hello')"
• "Delete the file old_data.txt"
• "Copy file1.txt to backup/file1.txt"
• "Move image.png to pictures folder"
• "Rename document.txt to report.txt"

*Directory Operations:*
• "What's the current directory?"
• "Change to C:\\Users\\Documents"
• "Create a new folder called Projects"
• "Delete the folder temp"
• "List all folders in C:\\Users"

*System Operations:*
• "Execute command: ipconfig"
• "Run the script: python test.py"
• "Change permissions of file.sh to 755"
• "Get information about data.csv"

*Security Operations:*
• "Encrypt all files in current directory"
• "Decrypt all files in current directory"

*Screen Operations:*
• "Take a screenshot and save it as screen.png"
• "Record screen for 10 seconds"

*Tips:*
✓ Be specific with file names and paths
✓ Use full paths when working with different directories
✓ The agent will confirm actions before destructive operations
✓ Check if files exist before trying to read or modify them

Need something else? Just ask naturally!
"""
    
    bot.reply_to(message, help_message, parse_mode='Markdown')


@bot.message_handler(commands=['clear'])
def clear_context(message):
    """Clear the conversation context for the user."""
    if not is_authorized(message.chat.id):
        bot.reply_to(message, "⛔ You are not authorized to use this bot.")
        return
    
    chat_id = message.chat.id
    if chat_id in user_contexts:
        del user_contexts[chat_id]
    
    bot.reply_to(message, "🗑️ Conversation context cleared! Starting fresh.")


@bot.message_handler(commands=['info'])
def system_info(message):
    """Get system information."""
    if not is_authorized(message.chat.id):
        bot.reply_to(message, "⛔ You are not authorized to use this bot.")
        return
    
    try:
        cwd = os.getcwd()
        info_message = f"""
💻 *System Information*

📂 Current Directory: `{cwd}`
🖥️ OS: {os.name}
👤 User: {os.getlogin() if hasattr(os, 'getlogin') else 'N/A'}

Use natural language to ask me to perform any system operation!
"""
        bot.reply_to(message, info_message, parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, f"❌ Error getting system info: {str(e)}")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """Handle all text messages using the AI agent."""
    chat_id = message.chat.id
    
    if not is_authorized(chat_id):
        bot.reply_to(message, "⛔ You are not authorized to use this bot.")
        return
    
    user_query = message.text
    
    # Show typing indicator
    bot.send_chat_action(chat_id, 'typing')
    
    try:
        # Send the query to the agent using Runner
        bot.reply_to(message, "🤖 Processing your request...")
        
        # Setup user and session IDs
        user_id = str(chat_id)
        session_id = f"session_{chat_id}"
        
        # Create user content
        content = types.Content(role='user', parts=[types.Part(text=user_query)])
        
        # Run the agent through the runner
        events = runner.run(
            user_id=user_id, 
            session_id=session_id, 
            new_message=content
        )
        
        # Collect the final response
        text_parts = []
        tool_messages = []
        debug_messages = []
        files_to_send = []

        for event in events:
            if not event.content:
                continue

            if event.is_final_response():
                for part in event.content.parts:
                    if getattr(part, 'text', None):
                        text_parts.append(part.text)
                    elif getattr(part, 'function_response', None):
                        function_response = part.function_response
                        response_payload = getattr(function_response, 'response', None)

                        if isinstance(response_payload, dict):
                            file_path = response_payload.get("file_path")
                            if file_path and os.path.exists(file_path):
                                files_to_send.append({
                                    "file_path": file_path,
                                    "caption": response_payload.get("message")
                                })

                            # Only show response details in debug mode
                            if DEBUG_MODE:
                                formatted_response = json.dumps(response_payload, indent=2)
                                debug_messages.append(formatted_response)
            else:
                for part in event.content.parts:
                    if getattr(part, 'function_call', None):
                        # Only show tool calls in debug mode
                        if DEBUG_MODE:
                            function_call = part.function_call
                            args_repr = function_call.args
                            try:
                                args_text = json.dumps(args_repr, indent=2)
                            except TypeError:
                                args_text = str(args_repr)
                            debug_messages.append(
                                f"🔧 Tool call: {function_call.name}\n{args_text}"
                            )
                    elif getattr(part, 'text', None):
                        text_parts.append(part.text)
                    elif getattr(part, 'function_response', None):
                        function_response = part.function_response
                        response_payload = getattr(function_response, 'response', None)

                        if isinstance(response_payload, dict):
                            file_path = response_payload.get("file_path")
                            if file_path and os.path.exists(file_path):
                                files_to_send.append({
                                    "file_path": file_path,
                                    "caption": response_payload.get("message")
                                })

                            # Only show response details in debug mode
                            if DEBUG_MODE:
                                formatted_response = json.dumps(response_payload, indent=2)
                                debug_messages.append(formatted_response)
        
        agent_response = "\n".join(part.strip() for part in text_parts if part and part.strip())
        
        # Only include debug info if DEBUG_MODE is enabled
        if DEBUG_MODE and debug_messages:
            extra_info = "\n\n".join(debug_messages)
            full_message = f"{agent_response}\n\n{extra_info}".strip() if agent_response else extra_info
        else:
            full_message = agent_response
        
        if not full_message:
            full_message = "I processed your request but couldn't generate a response. Please try again."
        
        # Send the response
        if len(full_message) > 4096:
            # Telegram message limit is 4096 characters
            # Save to file and send as document
            temp_file = f"response_{chat_id}_{int(time.time())}.txt"
            with open(temp_file, 'w', encoding='utf-8') as f:
                f.write(full_message)
            
            with open(temp_file, 'rb') as f:
                bot.send_document(chat_id, f, caption="📄 Response is too long, sent as file.")
            
            os.remove(temp_file)
        else:
            # Send without Markdown to avoid parsing errors
            bot.send_message(chat_id, full_message)

        for file_info in files_to_send:
            file_path = file_info.get("file_path")
            caption = file_info.get("caption")
            if not file_path or not os.path.exists(file_path):
                continue

            with open(file_path, 'rb') as f:
                if caption and len(caption) <= 1024:
                    bot.send_document(chat_id, f, caption=caption)
                else:
                    bot.send_document(chat_id, f)
    
    except Exception as e:
        # Escape special characters in error message
        error_text = f"❌ Error: {str(e)}\n\nPlease try again or rephrase your request."
        bot.reply_to(message, error_text)


@bot.message_handler(content_types=['document'])
def handle_document(message):
    """Handle document uploads."""
    if not is_authorized(message.chat.id):
        bot.reply_to(message, "⛔ You are not authorized to use this bot.")
        return
    
    try:
        bot.reply_to(message, "📥 Uploading file...")
        
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        file_name = message.document.file_name
        save_path = os.path.join(os.getcwd(), file_name)
        
        with open(save_path, 'wb') as f:
            f.write(downloaded_file)
        
        bot.reply_to(
            message,
            f"✅ File uploaded successfully!\n📁 Saved to: `{save_path}`",
            parse_mode='Markdown'
        )
    except Exception as e:
        bot.reply_to(message, f"❌ Failed to upload file: {str(e)}")


def start_bot():
    """Start the bot with error handling and auto-restart."""
    print("🤖 Telegram System Agent Bot Started...")
    print(f"📂 Working Directory: {os.getcwd()}")
    
    # Notify authorized users that bot is online
    for admin_id in AUTHORIZED_CHAT_IDS:
        if admin_id:
            try:
                bot.send_message(admin_id, "🟢 *System Agent Bot is Online*", parse_mode='Markdown')
            except:
                pass
    
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=60)
        except ConnectionError as e:
            print(f"⚠️ Connection error: {e}. Retrying in 5 seconds...")
            time.sleep(5)
        except Exception as e:
            print(f"❌ Unexpected error: {e}. Retrying in 5 seconds...")
            time.sleep(5)


if __name__ == "__main__":
    start_bot()
