"""
Quick Setup Script for Telegram System Agent

This script helps you set up the bot configuration quickly.
"""

import os
import sys


def setup_bot():
    print("=" * 60)
    print("🤖 Telegram System Agent - Setup Wizard")
    print("=" * 60)
    print()
    
    # Get Bot Token
    print("📝 Step 1: Telegram Bot Token")
    print("Get your bot token from @BotFather on Telegram")
    print("If you don't have one:")
    print("  1. Message @BotFather on Telegram")
    print("  2. Send /newbot")
    print("  3. Follow the instructions")
    print()
    bot_token = input("Enter your Bot Token: ").strip()
    
    if not bot_token:
        print("❌ Bot token is required!")
        return False
    
    # Get Chat IDs
    print()
    print("=" * 60)
    print("👤 Step 2: Authorized Users")
    print("Add Telegram chat IDs of users who can use the bot")
    print("To get your chat ID, message @userinfobot on Telegram")
    print()
    chat_ids = []
    
    while True:
        chat_id = input("Enter a chat ID (or press Enter to finish): ").strip()
        if not chat_id:
            break
        chat_ids.append(chat_id)
        print(f"✓ Added: {chat_id}")
    
    if not chat_ids:
        print("⚠️  Warning: No chat IDs added. Bot will accept requests from anyone!")
        print("   This is NOT recommended for security reasons.")
        proceed = input("Continue anyway? (yes/no): ").strip().lower()
        if proceed != 'yes':
            return False
    
    # Update telegram_bot.py
    print()
    print("=" * 60)
    print("💾 Step 3: Saving Configuration")
    
    try:
        # Read the current file
        bot_file = os.path.join(os.path.dirname(__file__), 'telegram_bot.py')
        with open(bot_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the configuration
        content = content.replace('BOT_TOKEN = ""', f'BOT_TOKEN = "{bot_token}"')
        
        if chat_ids:
            chat_ids_str = '", "'.join(chat_ids)
            content = content.replace(
                'AUTHORIZED_CHAT_IDS = [""]',
                f'AUTHORIZED_CHAT_IDS = ["{chat_ids_str}"]'
            )
        
        # Write back
        with open(bot_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Configuration saved successfully!")
        
    except Exception as e:
        print(f"❌ Error saving configuration: {e}")
        return False
    
    # Installation instructions
    print()
    print("=" * 60)
    print("📦 Step 4: Install Dependencies")
    print()
    print("Run the following command:")
    print("  pip install -r requirements.txt")
    print()
    
    install_now = input("Install dependencies now? (yes/no): ").strip().lower()
    
    if install_now == 'yes':
        print("\n🔄 Installing dependencies...")
        os.system("pip install -r requirements.txt")
    
    # Final instructions
    print()
    print("=" * 60)
    print("🎉 Setup Complete!")
    print("=" * 60)
    print()
    print("✅ Configuration saved")
    print("✅ Bot token configured")
    print(f"✅ {len(chat_ids)} authorized user(s) added")
    print()
    print("🚀 To start the bot, run:")
    print("   python main.py")
    print()
    print("📖 For more information, see README.md")
    print()
    
    return True


if __name__ == "__main__":
    try:
        success = setup_bot()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Setup failed: {e}")
        sys.exit(1)
