# Telegram System Agent with AI

An intelligent Telegram bot powered by Google's ADK Agent (Gemini) that provides comprehensive system control capabilities through natural language interaction. This project merges the functionality of HackTheSystem with an intelligent agent mode similar to multi-tool-agent.

## 🌟 Features

### 🤖 AI-Powered Intelligence
- Natural language processing using Google Gemini
- Context-aware responses
- Intelligent task execution
- Multi-step operation handling

### 📁 File & Directory Management
- List, create, read, write, and delete files
- Directory operations (create, delete, navigate)
- Copy and move files
- Batch rename operations
- File information retrieval

### 💻 System Operations
- Execute shell commands remotely
- Change file permissions (chmod)
- Check file/directory existence
- Get current working directory

### 🔐 Security Operations
- File encryption (ransomware-like functionality for testing)
- File decryption
- Secure file handling

### 📸 Screen Operations
- Capture screenshots
- Record screen with customizable duration
- Save media files and send via Telegram

### 🔒 Security Features
- Chat ID-based authorization
- Authorized user management
- Activity logging and notifications

## 📋 Prerequisites

- Python 3.8 or higher
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- Google API Key (for Gemini/ADK)
- Windows/Linux/Mac OS

## 🚀 Installation

### 1. Clone or Download the Repository

```bash
cd "E:\CodingWorld\Pyhton Projects\AI-Agents\telegram-agent"
```

### 2. Install Dependencies

**Windows:**
```powershell
pip install -r requirements.txt
```

**Linux/Mac:**
```bash
pip3 install -r requirements.txt
```

### 3. Configure the Bot

Edit `config.py` and add your credentials:

```python
# Telegram Bot Configuration
BOT_TOKEN = "your_bot_token_here"  # Get from @BotFather

# Authorized Users
AUTHORIZED_CHAT_IDS = [
    "123456789",  # Your Telegram chat ID
    "987654321",  # Another authorized user
]
```

**Getting Your Chat ID:**
1. Message [@userinfobot](https://t.me/userinfobot) on Telegram
2. It will reply with your chat ID
3. Add it to the `AUTHORIZED_CHAT_IDS` list

### 4. Set Up Google ADK (Optional but Recommended)

If using Google's Agent Development Kit:
```bash
# Set up Google Cloud credentials
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
```

## 💡 Usage

### Starting the Bot

**Windows:**
```powershell
python main.py
```

**Linux/Mac:**
```bash
python3 main.py
```

**Background Mode (Linux/Mac):**
```bash
nohup python3 main.py &
```

**Windows Background Mode:**
Create a `.pyw` version and run it:
```powershell
pythonw main.pyw
```

### Telegram Commands

#### Quick Commands
- `/start` - Welcome message and bot introduction
- `/help` - Detailed help and examples
- `/clear` - Clear conversation context
- `/info` - Get system information

#### Natural Language Examples

**File Operations:**
```
"Show me all files in the current directory"
"Create a file called test.txt with the content Hello World"
"Read the file config.json"
"Delete the old_data.txt file"
"Copy report.pdf to the backup folder"
```

**Directory Operations:**
```
"What's the current directory?"
"Change to C:\Users\Documents"
"Create a new folder called Projects"
"List all folders in D:\Work"
```

**System Operations:**
```
"Execute the command: ipconfig"
"Run python script.py"
"Get information about data.csv"
"Change permissions of file.sh to 755"
```

**Security Operations:**
```
"Encrypt all files in the current directory"
"Decrypt the encrypted files"
```

**Screen Operations:**
```
"Take a screenshot"
"Record my screen for 15 seconds"
```

## 🏗️ Project Structure

```
telegram-agent/
│
├── __init__.py              # Package initialization
├── main.py                  # Main entry point
├── telegram_bot.py          # Telegram bot logic
├── agent.py                 # AI agent configuration
├── system_tools.py          # System operation tools
├── config.py                # Configuration file
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🔧 Configuration Options

Edit `config.py` to customize:

- `BOT_TOKEN`: Your Telegram bot token
- `AUTHORIZED_CHAT_IDS`: List of allowed user IDs
- `AGENT_MODEL`: Gemini model to use
- `MAX_FILE_SIZE_MB`: Maximum upload file size
- `DEFAULT_RECORDING_DURATION`: Default screen recording time
- `MAX_RECORDING_DURATION`: Maximum allowed recording time
- `RECORDING_FPS`: Screen recording frame rate

## 🛡️ Security Considerations

⚠️ **IMPORTANT SECURITY NOTES:**

1. **Authorization**: Always keep `REQUIRE_AUTHORIZATION = True`
2. **Chat IDs**: Only add trusted users to `AUTHORIZED_CHAT_IDS`
3. **Bot Token**: Never share your bot token publicly
4. **Sensitive Operations**: Be cautious with:
   - File deletion
   - File encryption
   - Command execution
   - Permission changes

5. **Network**: Run on trusted networks only
6. **Monitoring**: Check bot activity logs regularly

## 🐛 Troubleshooting

### Bot doesn't respond
- Check if the bot token is correct
- Verify your chat ID is in the authorized list
- Check internet connection
- Look for errors in the console

### Commands fail
- Verify file paths are correct
- Check file permissions
- Ensure required dependencies are installed
- Check if the current directory is accessible

### Screen recording issues
- Verify `opencv-python` and `pyautogui` are installed
- Check if screen resolution is supported
- Reduce recording duration for large files

### Import errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version (3.8+)
- Try reinstalling packages

## 🔄 Auto-Start on System Boot

### Windows

1. Create a batch file `start_bot.bat`:
```batch
@echo off
cd "E:\CodingWorld\Pyhton Projects\AI-Agents\telegram-agent"
pythonw main.py
```

2. Press `Win + R`, type `shell:startup`, and press Enter
3. Copy `start_bot.bat` to the Startup folder

### Linux (systemd)

1. Create a service file `/etc/systemd/system/telegram-agent.service`:
```ini
[Unit]
Description=Telegram System Agent
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/telegram-agent
ExecStart=/usr/bin/python3 main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

2. Enable and start:
```bash
sudo systemctl enable telegram-agent
sudo systemctl start telegram-agent
```

## 📚 Examples

### Example Conversation

```
User: Show me the current directory
Bot: 🤖 Processing your request...
Bot: The current working directory is: C:\Users\YourName\Documents

User: Create a file named notes.txt with the content "Meeting at 3pm"
Bot: 🤖 Processing your request...
Bot: ✅ Successfully created file: C:\Users\YourName\Documents\notes.txt

User: Take a screenshot
Bot: 🤖 Processing your request...
Bot: ✅ Screenshot saved to: screenshot.png
[Sends the screenshot file]
```

## 🤝 Contributing

This project combines functionality from:
- **HackTheSystem**: Telegram bot for system control
- **multi-tool-agent**: AI agent framework

Feel free to submit issues, fork the repository, and create pull requests!

## 📄 License

This project is for educational purposes only. Use responsibly and only on systems you own or have permission to access.

## ⚠️ Disclaimer

This tool is intended for legitimate system administration and educational purposes only. Misuse of this software for unauthorized access to systems is illegal and unethical. The authors are not responsible for any misuse or damage caused by this software.

## 👨‍💻 Author

Created by merging HackTheSystem with AI agent capabilities.

Repository: [AI-Agents](https://github.com/atrajit-sarkar/AI-Agents)

## 📞 Support

For issues and questions:
1. Check the Troubleshooting section
2. Review the examples
3. Open an issue on GitHub

---

**Happy Coding! 🚀**
