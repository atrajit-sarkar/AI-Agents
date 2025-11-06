"""
Configuration file for Telegram System Agent

IMPORTANT: Fill in your credentials here before running the bot!
"""

# Telegram Bot Configuration
BOT_TOKEN = ""  # Get this from @BotFather on Telegram

# Authorized Users (Chat IDs)
# Add Telegram chat IDs of users who are allowed to use the bot
# You can get your chat ID by messaging @userinfobot on Telegram
AUTHORIZED_CHAT_IDS = [
    # "123456789",  # Example chat ID
    # "987654321",  # Another example
]

# Agent Configuration
AGENT_MODEL = "gemini-2.0-flash"  # Gemini model to use
AGENT_NAME = "telegram_system_agent"

# Security Settings
REQUIRE_AUTHORIZATION = True  # Set to False to allow anyone to use the bot (NOT RECOMMENDED)

# Logging Configuration
ENABLE_LOGGING = True
LOG_FILE = "telegram_agent.log"

# File Upload Settings
MAX_FILE_SIZE_MB = 20  # Maximum file size for uploads in MB
UPLOAD_DIRECTORY = "uploads"  # Directory to save uploaded files

# Screen Recording Settings
DEFAULT_RECORDING_DURATION = 10  # Default recording duration in seconds
MAX_RECORDING_DURATION = 60  # Maximum allowed recording duration
RECORDING_FPS = 7  # Frames per second for screen recording
RECORDING_RESOLUTION = (1920, 1080)  # Screen recording resolution

# Response Settings
MAX_MESSAGE_LENGTH = 4096  # Telegram's message limit
LONG_RESPONSE_AS_FILE = True  # Send long responses as text files
