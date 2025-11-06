#!/usr/bin/env python3
"""
Telegram System Agent - Main Entry Point

This is an intelligent Telegram bot that uses Google's ADK Agent to provide
system control capabilities through natural language interaction.

Features:
- File and directory management
- Command execution
- File encryption/decryption
- Screen capture and recording
- Natural language interface
- Secure authorization system

Usage:
1. Add your Telegram Bot Token in telegram_bot.py
2. Add authorized chat IDs in telegram_bot.py
3. Run: python main.py

Author: Based on HackTheSystem and multi-tool-agent
"""

import sys
import os
from pathlib import Path

# Add the current directory to the path to allow imports
sys.path.insert(0, str(Path(__file__).parent))

# Import directly without relative imports
import telegram_bot


def main():
    """Main entry point for the Telegram System Agent."""
    print("=" * 60)
    print("🤖 Telegram System Agent with AI")
    print("=" * 60)
    print()
    print("📋 Features:")
    print("  ✓ Intelligent AI-powered responses")
    print("  ✓ File & directory management")
    print("  ✓ Command execution")
    print("  ✓ File encryption/decryption")
    print("  ✓ Screen capture & recording")
    print("  ✓ Natural language interface")
    print()
    print("⚠️  Security Notice:")
    print("  Make sure to configure BOT_TOKEN and AUTHORIZED_CHAT_IDS")
    print("  in telegram_bot.py before running!")
    print()
    print("=" * 60)
    print()
    
    try:
        telegram_bot.start_bot()
    except KeyboardInterrupt:
        print("\n\n🛑 Bot stopped by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
