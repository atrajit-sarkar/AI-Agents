# File Upload & Download Guide

This guide explains how to upload and download files using the Telegram System Agent.

## 📤 Uploading Files to the System

### Method: Direct File Send

Simply send any file/document to the bot via Telegram:

1. Open the chat with your bot
2. Click the attachment icon (📎)
3. Select the file you want to upload
4. Send it to the bot

The bot will:
- Download the file
- Save it to the current working directory
- Confirm the upload with the full path

**Example:**
```
You: [Sends document: report.pdf]
Bot: 📥 Uploading file...
Bot: ✅ File uploaded successfully!
     📁 Saved to: E:\CodingWorld\Projects\report.pdf
```

**Supported File Types:**
- Documents (PDF, DOCX, TXT, etc.)
- Images (JPG, PNG, GIF, etc.)
- Videos (MP4, AVI, MKV, etc.)
- Archives (ZIP, RAR, 7Z, etc.)
- Code files (PY, JS, HTML, etc.)
- Any other file type

**Notes:**
- Files are saved with their original names
- If a file with the same name exists, it will be overwritten
- Large files may take time to upload depending on your connection

---

## 📥 Downloading Files from the System

### Method 1: Download Single File

Ask the bot to download a specific file:

**Natural Language Examples:**
```
"Download config.txt"
"Send me the file report.pdf"
"Fetch document.docx"
"Get me data.csv"
"Download E:\Projects\main.py"
```

**What Happens:**
1. Bot locates the file
2. Validates it exists and is accessible
3. Sends the file to you via Telegram
4. Shows file size and path information

**Example Interaction:**
```
You: Download report.pdf
Bot: 🔧 Tool call: download_file
     {
       "file_path": "report.pdf"
     }
     
     {
       "status": "success",
       "file_path": "E:\\Projects\\report.pdf",
       "file_name": "report.pdf",
       "size_mb": 2.45,
       "message": "File ready for download: E:\\Projects\\report.pdf (2.45 MB)"
     }
     
     [Bot sends the file as a document]
```

---

### Method 2: Download Entire Directory

Ask the bot to download all files from a directory as a ZIP archive:

**Natural Language Examples:**
```
"Download the Documents folder"
"Fetch all files from the project directory"
"Download E:\Data as a zip"
"Get me the entire Downloads folder"
```

**What Happens:**
1. Bot creates a ZIP archive of the directory
2. Compresses all files and subdirectories
3. Sends the ZIP file to you via Telegram
4. Shows archive size

**Example Interaction:**
```
You: Download the project folder as a zip
Bot: 🔧 Tool call: download_directory
     {
       "directory_path": "project"
     }
     
     {
       "status": "success",
       "file_path": "project.zip",
       "directory": "E:\\Projects\\project",
       "size_mb": 15.8,
       "message": "Directory archived for download: project.zip (15.8 MB)"
     }
     
     [Bot sends project.zip]
```

**Custom ZIP Names:**
```
"Download the data folder as backup.zip"
"Archive the logs directory to logs_archive.zip"
```

---

### Method 3: List Files Before Downloading

Preview what's in a directory before downloading:

**Natural Language Examples:**
```
"List files in the Downloads folder"
"Show me what's in the Documents directory"
"What files are in E:\Data?"
```

**Example Interaction:**
```
You: List files in the project folder
Bot: 🔧 Tool call: list_files_in_directory
     {
       "directory_path": "project"
     }
     
     {
       "status": "success",
       "directory": "E:\\Projects\\project",
       "items": [
         {
           "name": "src",
           "type": "directory",
           "size_bytes": 0,
           "size_mb": 0,
           "modified": "Wed Nov  6 10:30:00 2024"
         },
         {
           "name": "main.py",
           "type": "file",
           "size_bytes": 4567,
           "size_mb": 0.004,
           "modified": "Wed Nov  6 11:20:00 2024"
         },
         {
           "name": "README.md",
           "type": "file",
           "size_bytes": 2340,
           "size_mb": 0.002,
           "modified": "Wed Nov  6 09:15:00 2024"
         }
       ],
       "total_items": 3,
       "message": "Found 3 items in E:\\Projects\\project"
     }
```

---

## 🎯 Common Use Cases

### Backup Important Files
```
You: Download my important documents folder as backup.zip
Bot: [Creates and sends backup.zip with all files]
```

### Retrieve Generated Files
```
You: Take a screenshot
Bot: [Takes screenshot and sends screenshot.png]

You: Record screen for 10 seconds
Bot: [Records and sends recording.mp4]
```

### Get Configuration Files
```
You: Download config.json
Bot: [Sends config.json]
```

### Batch Download
```
You: List files in the reports folder
Bot: [Shows: report1.pdf, report2.pdf, report3.pdf]

You: Download the reports folder
Bot: [Sends reports.zip with all files]
```

### Upload and Process
```
You: [Uploads script.py]
Bot: ✅ File uploaded successfully!

You: Execute script.py
Bot: [Runs the script and shows output]
```

---

## 💡 Tips & Best Practices

### For Uploading:
1. **Check current directory first:**
   ```
   "What's my current directory?"
   "pwd"
   ```

2. **Change directory before uploading:**
   ```
   "Change directory to E:\Projects"
   [Then send your file]
   ```

3. **Verify upload:**
   ```
   "List files in current directory"
   ```

### For Downloading:
1. **Use relative paths when in the directory:**
   ```
   "Download config.txt"  ✅ Simple
   ```

2. **Use absolute paths from anywhere:**
   ```
   "Download E:\Projects\config.txt"  ✅ Specific
   ```

3. **Check file size before downloading large directories:**
   ```
   "List files in the videos folder"
   [Check sizes, then:]
   "Download the videos folder"
   ```

4. **Download specific files instead of entire directories for faster transfers:**
   ```
   "Download report.pdf"  ✅ Fast
   vs
   "Download the documents folder"  ⚠️ Might be large
   ```

---

## 🚨 Limitations & Considerations

### File Size Limits:
- **Telegram Limit:** 2 GB per file (50 MB for free users)
- **Large directories:** Will be compressed, but might still exceed limits
- **Solution:** Download specific files instead of entire directories

### Network Considerations:
- Large files take time to transfer
- Unstable connections might interrupt transfers
- Bot will retry failed uploads automatically

### Storage:
- Uploaded files use system disk space
- Clean up unnecessary files regularly
- Use encryption feature for sensitive files

### Security:
- Only authorized users can upload/download
- All transfers are logged
- Files are saved with original names (watch for overwrites)

---

## 🔐 Security Tips

1. **Don't upload sensitive data without encryption:**
   ```
   [Upload sensitive files]
   "Encrypt all files in current directory"
   ```

2. **Clean up after downloads:**
   ```
   "Delete confidential.zip"
   "Remove all zip files"
   ```

3. **Verify file paths:**
   ```
   "Show me the full path of the file"
   "Get file info for secret.txt"
   ```

4. **Use secure connections:**
   - Use VPN when accessing sensitive systems
   - Only authorize trusted Telegram accounts

---

## 📞 Troubleshooting

### Upload Issues:

**Problem:** File upload fails
- **Check:** File size (under 2GB)
- **Check:** Disk space on system
- **Check:** File is not locked by another program

**Problem:** Upload succeeds but file not found
- **Solution:** Check current directory: "pwd"
- **Solution:** List files: "list files in current directory"

### Download Issues:

**Problem:** "File not found" error
- **Solution:** Verify path: "Does E:\file.txt exist?"
- **Solution:** List directory: "List files in E:\"

**Problem:** Download times out
- **Solution:** File might be too large
- **Solution:** Try compressing first: "zip the file"
- **Solution:** Split into smaller parts

**Problem:** Can't download directory
- **Solution:** Check if it's a valid directory
- **Solution:** Try downloading files individually
- **Solution:** Create manual zip: "Create archive of the folder"

---

## 🎓 Advanced Examples

### Backup Workflow:
```
You: Change directory to E:\Projects
Bot: ✅ Changed directory

You: List files in current directory
Bot: [Shows all files and folders]

You: Download the entire project as backup_2024.zip
Bot: [Creates and sends backup_2024.zip]

You: Take a screenshot
Bot: [Sends screenshot.png]
```

### Remote File Management:
```
You: Create file todo.txt with content "Buy milk"
Bot: ✅ File created

You: Download todo.txt
Bot: [Sends todo.txt]

You: Read file todo.txt
Bot: Content: "Buy milk"

You: Delete todo.txt
Bot: ✅ File deleted
```

### Batch Processing:
```
You: List files in the images folder
Bot: [Shows: img1.jpg, img2.jpg, img3.jpg]

You: Download the images folder
Bot: [Sends images.zip]

You: Rename all files in images folder to photo
Bot: [Renames: photo0.jpg, photo1.jpg, photo2.jpg]

You: Download the images folder
Bot: [Sends updated images.zip]
```

---

## 📚 Related Commands

- `pwd` or "What's my current directory?" - Show working directory
- `cd <path>` or "Change directory to <path>" - Change directory
- `ls` or "List files" - List directory contents
- `file_exists <path>` or "Does <file> exist?" - Check file existence
- `get_file_info <path>` or "Show info for <file>" - Get file details

---

## 🆘 Need Help?

If you encounter issues:
1. Check the main README.md for setup instructions
2. Verify your authorization (chat ID in config.py)
3. Check bot console for error messages
4. Ensure file paths are correct for your OS
5. Test with small files first

For questions or issues, check the project documentation or console logs.
