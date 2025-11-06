"""
Example Usage Scenarios for Telegram System Agent

This file demonstrates various ways to interact with the bot
and showcases its capabilities.
"""

# ============================================================================
# BASIC FILE OPERATIONS
# ============================================================================

"""
User: "What's the current directory?"
Bot: "The current working directory is: C:\Users\YourName\Documents"

User: "Show me all files here"
Bot: "Found 3 folders and 5 files in C:\Users\YourName\Documents
     Folders: Projects, Backup, Archive
     Files: notes.txt, report.pdf, data.csv, image.png, script.py"

User: "Create a file called todo.txt with Task 1: Complete project"
Bot: "✅ Successfully created file: C:\Users\YourName\Documents\todo.txt"

User: "Read the file todo.txt"
Bot: "📄 File content:
     Task 1: Complete project"

User: "Add more tasks to todo.txt: Task 2: Review code, Task 3: Deploy"
Bot: "✅ Successfully wrote to file: C:\Users\YourName\Documents\todo.txt"
"""

# ============================================================================
# DIRECTORY OPERATIONS
# ============================================================================

"""
User: "Create a new folder called ProjectBackup"
Bot: "✅ Successfully created directory: C:\Users\YourName\Documents\ProjectBackup"

User: "Change to the ProjectBackup folder"
Bot: "✅ Changed directory to: C:\Users\YourName\Documents\ProjectBackup"

User: "Go back to the parent directory"
Bot: "✅ Changed directory to: C:\Users\YourName\Documents"

User: "List all directories in C:\Users"
Bot: "Found 8 folders and 2 files in C:\Users
     Folders: Public, YourName, Administrator, Default, ..."
"""

# ============================================================================
# FILE MANAGEMENT
# ============================================================================

"""
User: "Copy report.pdf to the Backup folder"
Bot: "✅ Successfully copied report.pdf to Backup\report.pdf"

User: "Move old_notes.txt to Archive folder"
Bot: "✅ Successfully moved old_notes.txt to Archive\old_notes.txt"

User: "Does the file important.doc exist?"
Bot: "✅ Path exists: C:\Users\YourName\Documents\important.doc"

User: "Delete the file temp.txt"
Bot: "✅ Successfully deleted file: C:\Users\YourName\Documents\temp.txt"

User: "Get information about large_file.zip"
Bot: "📊 File Information:
     Path: C:\Users\YourName\Documents\large_file.zip
     Size: 45.67 MB
     Modified: Mon Jan 15 14:30:25 2024
     Created: Mon Jan 15 10:15:00 2024"
"""

# ============================================================================
# SYSTEM COMMANDS
# ============================================================================

"""
User: "Execute command: ipconfig"
Bot: "✅ Command executed: ipconfig
     
     Output:
     Windows IP Configuration
     
     Ethernet adapter Ethernet:
        IPv4 Address. . . . . . . . . . . : 192.168.1.100
        Subnet Mask . . . . . . . . . . . : 255.255.255.0
        Default Gateway . . . . . . . . . : 192.168.1.1"

User: "Run the command: python --version"
Bot: "✅ Command executed: python --version
     Output: Python 3.11.5"

User: "Execute: dir /b"
Bot: "✅ Command executed: dir /b
     Output:
     Projects
     Backup
     notes.txt
     report.pdf
     ..."
"""

# ============================================================================
# SECURITY OPERATIONS
# ============================================================================

"""
User: "Encrypt all files in the current directory"
Bot: "🔐 Processing encryption...
     ✅ Successfully encrypted 5 out of 5 files in C:\Users\YourName\Documents
     ⚠️  Keep the secretkey.key file safe! You'll need it to decrypt."

User: "Decrypt the encrypted files"
Bot: "🔓 Processing decryption...
     ✅ Successfully decrypted 5 out of 5 files in C:\Users\YourName\Documents"
"""

# ============================================================================
# SCREEN OPERATIONS
# ============================================================================

"""
User: "Take a screenshot"
Bot: "📸 Capturing screenshot...
     ✅ Screenshot saved to: screenshot.png"
     [Bot sends the screenshot file]

User: "Record my screen for 15 seconds"
Bot: "🎥 Recording screen...
     ⏱️  Recording for 15 seconds...
     ✅ Screen recorded and saved to: recording.mp4"
     [Bot sends the video file]

User: "Take a screenshot and save it as desktop.png"
Bot: "📸 Capturing screenshot...
     ✅ Screenshot saved to: desktop.png"
     [Bot sends the screenshot file]
"""

# ============================================================================
# ADVANCED FILE OPERATIONS
# ============================================================================

"""
User: "Rename all files in the temp folder with prefix backup_"
Bot: "🔄 Batch renaming files...
     ✅ Successfully renamed 12 items in C:\Users\YourName\temp
     Files renamed: file1.txt -> backup_0.txt, file2.txt -> backup_1.txt, ..."

User: "Change permissions of script.sh to 755"
Bot: "✅ Successfully changed permissions of script.sh to 755"

User: "Copy all .txt files from Documents to Backup"
Bot: "This requires multiple steps. Let me do that for you...
     📋 Found 5 .txt files
     ✅ Copied notes.txt
     ✅ Copied todo.txt
     ✅ Copied data.txt
     ✅ Copied report.txt
     ✅ Copied summary.txt
     ✅ All .txt files copied successfully!"
"""

# ============================================================================
# COMPLEX MULTI-STEP OPERATIONS
# ============================================================================

"""
User: "Create a project structure with folders: src, tests, docs, and data"
Bot: "🏗️  Creating project structure...
     ✅ Created directory: src
     ✅ Created directory: tests
     ✅ Created directory: docs
     ✅ Created directory: data
     ✅ Project structure created successfully!"

User: "Create a Python script in src folder called hello.py with print hello world"
Bot: "✅ Successfully created file: src\hello.py
     Content written: print('Hello World')"

User: "Now execute that script"
Bot: "✅ Command executed: python src\hello.py
     Output: Hello World"
"""

# ============================================================================
# ERROR HANDLING EXAMPLES
# ============================================================================

"""
User: "Read the file nonexistent.txt"
Bot: "❌ Error: Failed to read file: [Errno 2] No such file or directory: 'nonexistent.txt'"

User: "Change to Z:\InvalidPath"
Bot: "❌ Error: Failed to change directory: [WinError 3] The system cannot find the path specified"

User: "Delete protected_system_file.sys"
Bot: "❌ Error: Failed to delete file: [WinError 5] Access is denied"
"""

# ============================================================================
# UTILITY COMMANDS
# ============================================================================

"""
User: "/start"
Bot: Shows welcome message with feature list

User: "/help"
Bot: Shows detailed help with examples

User: "/info"
Bot: "💻 System Information
     📂 Current Directory: C:\Users\YourName\Documents
     🖥️ OS: nt
     👤 User: YourName"

User: "/clear"
Bot: "🗑️ Conversation context cleared! Starting fresh."
"""

# ============================================================================
# PRACTICAL USE CASES
# ============================================================================

"""
# 1. DAILY BACKUP ROUTINE
User: "Create a backup of all my documents"
Bot: Creates backup folder, copies files, confirms completion

# 2. SYSTEM MONITORING
User: "Show me disk space usage"
Bot: Executes df command and shows results

# 3. QUICK FILE SEARCH
User: "Find all .log files in C:\Windows\Temp"
Bot: Lists all log files found

# 4. REMOTE FILE EDITING
User: "Read config.json, change the port to 8080, and save it"
Bot: Reads file, modifies content, saves it back

# 5. BATCH OPERATIONS
User: "Delete all .tmp files in the temp folder"
Bot: Finds and deletes all temporary files

# 6. SYSTEM DIAGNOSTICS
User: "Check if Python is installed and show version"
Bot: Runs command and displays Python version

# 7. QUICK NOTES
User: "Create a note: Meeting tomorrow at 3pm with the team"
Bot: Creates or appends to notes.txt

# 8. SECURITY AUDIT
User: "List all .exe files in Downloads folder"
Bot: Searches and lists all executable files
"""

# ============================================================================
# TIPS FOR EFFECTIVE USE
# ============================================================================

"""
TIPS:
1. Be specific with file paths - use full paths when possible
2. Use natural language - the AI understands context
3. For sensitive operations, the bot will ask for confirmation
4. Long outputs are sent as text files automatically
5. You can upload files directly to the bot
6. Use /clear to reset context if the bot gets confused
7. Check /info regularly to know your current directory
8. For batch operations, explain clearly what you want to achieve
9. The bot remembers previous commands in the session
10. Use screenshots to verify UI operations
"""

print(__doc__)
