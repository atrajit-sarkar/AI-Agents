# 🚀 Quick Start Guide - Telegram System Agent

## 🎯 Goal
Set up and run your intelligent Telegram bot in 5 minutes!

---

## 📋 Prerequisites Checklist

- [ ] Python 3.8+ installed
- [ ] Telegram account
- [ ] 5 minutes of your time

---

## ⚡ Quick Setup (3 Steps)

### Step 1: Get Your Bot Token (2 minutes)

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` command
3. Choose a name for your bot (e.g., "My System Agent")
4. Choose a username (must end with 'bot', e.g., "my_system_agent_bot")
5. Copy the bot token (looks like: `123456789:ABCdefGhIJKlmNoPQRstuVWXyz`)

### Step 2: Get Your Chat ID (1 minute)

1. Search for `@userinfobot` on Telegram
2. Send any message to it
3. It will reply with your chat ID (e.g., `123456789`)
4. Copy this number

### Step 3: Configure and Run (2 minutes)

**Option A: Using Setup Script (Recommended)**

```powershell
# Navigate to the folder
cd "E:\CodingWorld\Pyhton Projects\AI-Agents\telegram-agent"

# Run setup
python setup.py
```

Follow the prompts:
1. Paste your bot token
2. Paste your chat ID
3. Let it install dependencies
4. Done! 🎉

**Option B: Manual Setup**

```powershell
# 1. Install dependencies
pip install -r requirements.txt

# 2. Edit telegram_bot.py
# Find these lines and add your values:
BOT_TOKEN = "your_bot_token_here"
AUTHORIZED_CHAT_IDS = ["your_chat_id_here"]

# 3. Run the bot
python main.py
```

---

## 🎮 Using Your Bot

### First Message

Open Telegram, find your bot, and send:
```
/start
```

You should see a welcome message! 🎉

### Try These Commands

```
"Show me the current directory"
"List all files here"
"Create a file called test.txt with Hello World"
"Take a screenshot"
```

The bot will respond intelligently to your natural language commands!

---

## 🔥 Pro Tips

### 1. Run in Background (Windows)

Create `start_bot.bat`:
```batch
@echo off
cd "E:\CodingWorld\Pyhton Projects\AI-Agents\telegram-agent"
pythonw main.py
```
Double-click to run!

### 2. Auto-Start with Windows

1. Press `Win + R`
2. Type `shell:startup` and press Enter
3. Copy your `start_bot.bat` file there

### 3. Check if Bot is Running

Look for: `🤖 Telegram System Agent Bot Started...` in console

### 4. Stop the Bot

Press `Ctrl + C` in the console

---

## ❓ Common Issues & Quick Fixes

### Bot doesn't respond?

**Check 1:** Is your bot token correct?
```powershell
# Look in telegram_bot.py, line ~10
BOT_TOKEN = "..."  # Should not be empty
```

**Check 2:** Is your chat ID in the authorized list?
```powershell
# Look in telegram_bot.py, line ~11
AUTHORIZED_CHAT_IDS = ["123456789"]  # Your ID should be here
```

**Check 3:** Is the bot running?
- You should see logs in the console
- The bot sent you "🟢 System Agent Bot is Online"

### Import errors?

```powershell
pip install -r requirements.txt --upgrade
```

### Permission errors?

Run as Administrator (right-click Python and "Run as administrator")

---

## 🎯 What's Next?

### Explore Features

1. **File Management**
   - `"Create a backup folder"`
   - `"Copy all .txt files to backup"`

2. **System Control**
   - `"Execute command: ipconfig"`
   - `"Get system information"`

3. **Security**
   - `"Encrypt files in current directory"`
   - `"Decrypt them back"`

4. **Screen Operations**
   - `"Take a screenshot"`
   - `"Record screen for 10 seconds"`

### Read the Full Documentation

Check out `README.md` for:
- Complete feature list
- Advanced configuration
- Security best practices
- Troubleshooting guide

---

## 🆘 Need Help?

1. Check console logs for errors
2. Read `README.md` for detailed docs
3. Try `/help` command in the bot
4. Open an issue on GitHub

---

## 🎉 You're All Set!

Your bot is now ready to control your system via Telegram!

**Security Reminder:** 
- Never share your bot token
- Only add trusted users to authorized list
- Monitor bot activity regularly

**Enjoy your intelligent Telegram bot! 🚀**

---

*For detailed information, see [README.md](README.md)*
