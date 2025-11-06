import os
import shutil
import json
from pathlib import Path
from typing import Union, List, Dict, Optional


def get_cwd() -> dict:
    """This returns the current working directory.
    
    Returns:
        dict: status and cwd(current working directory)
    """
    try:
        cwd = os.getcwd()
        return {
            "status": "success",
            "cwd": cwd
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Working Directory fetch issue: {str(e)}"
        }


def mkdir(dir_location: str, dir_name: str) -> dict:
    """This function makes folder in the directory specified as argument with the specified name.
    
    Args:
        dir_location (str): The specified directory where the folder creation should be run
        dir_name (str): The name of the folder to be created
    
    Returns:
        dict: status and message
    """
    try:
        full_path = os.path.join(dir_location, dir_name)
        os.makedirs(full_path, exist_ok=True)
        return {
            "status": "success",
            "path": full_path
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to create directory: {str(e)}"
        }


def chdir(dir_name: str) -> dict:
    """Change the current working directory to the specific directory passed as argument.
    
    Args:
        dir_name (str): The directory name specified by user
    
    Returns:
        dict: status and current directory
    """
    try:
        os.chdir(dir_name)
        return {
            "status": "success",
            "current_dir": os.getcwd()
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to change directory: {str(e)}"
        }


def create_file(file_name: str, content: str = "") -> dict:
    """This creates a file with user specified contents passed in the argument.
    
    Args:
        file_name (str): The user specified file name to be created
        content (str): The user specified content to be written as file content (default: "")
    
    Returns:
        dict: status and file path
    """
    try:
        # Create parent directories if they don't exist
        file_path = Path(file_name)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content)
        return {
            "status": "success",
            "file_path": str(file_path.absolute())
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to create file: {str(e)}"
        }


def read_file(file_path: str) -> dict:
    """Read the contents of a file.
    
    Args:
        file_path (str): The path to the file to read
    
    Returns:
        dict: status, content, and file info
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        file_size = os.path.getsize(file_path)
        return {
            "status": "success",
            "content": content,
            "file_path": file_path,
            "file_size": file_size
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to read file: {str(e)}"
        }


def write_file(file_path: str, content: str, mode: str = "w") -> dict:
    """Write content to a file (overwrite or append).
    
    Args:
        file_path (str): The path to the file
        content (str): The content to write
        mode (str): Write mode - 'w' for overwrite, 'a' for append (default: 'w')
    
    Returns:
        dict: status and message
    """
    try:
        # Create parent directories if they don't exist
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, mode, encoding="utf-8") as f:
            f.write(content)
        return {
            "status": "success",
            "file_path": file_path,
            "mode": "appended" if mode == "a" else "written"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to write file: {str(e)}"
        }


def delete_file(file_path: str) -> dict:
    """Delete a file with the specified path.
    
    Args:
        file_path (str): The user specified file path
    
    Returns:
        dict: status and message
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            return {
                "status": "success",
                "message": f"File '{file_path}' deleted successfully"
            }
        else:
            return {
                "status": "error",
                "message": f"File '{file_path}' does not exist"
            }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to delete file: {str(e)}"
        }


def delete_files(file_path_list: List[str]) -> dict:
    """Delete multiple files with the specified paths.
    
    Args:
        file_path_list (List[str]): List of file paths to delete
    
    Returns:
        dict: status, success count, and failed files
    """
    deleted = []
    failed = []
    
    try:
        for file_path in file_path_list:
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
                    deleted.append(file_path)
                else:
                    failed.append({"file": file_path, "reason": "File does not exist"})
            except Exception as e:
                failed.append({"file": file_path, "reason": str(e)})
        
        return {
            "status": "success" if len(failed) == 0 else "partial",
            "deleted_count": len(deleted),
            "failed_count": len(failed),
            "deleted_files": deleted,
            "failed_files": failed
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to delete files: {str(e)}"
        }


def copy_file(source: str, destination: str) -> dict:
    """Copy a file from source to destination.
    
    Args:
        source (str): Source file path
        destination (str): Destination file path
    
    Returns:
        dict: status and message
    """
    try:
        # Create destination directory if it doesn't exist
        Path(destination).parent.mkdir(parents=True, exist_ok=True)
        
        shutil.copy2(source, destination)
        return {
            "status": "success",
            "source": source,
            "destination": destination,
            "message": "File copied successfully"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to copy file: {str(e)}"
        }


def move_file(source: str, destination: str) -> dict:
    """Move a file from source to destination.
    
    Args:
        source (str): Source file path
        destination (str): Destination file path
    
    Returns:
        dict: status and message
    """
    try:
        # Create destination directory if it doesn't exist
        Path(destination).parent.mkdir(parents=True, exist_ok=True)
        
        shutil.move(source, destination)
        return {
            "status": "success",
            "source": source,
            "destination": destination,
            "message": "File moved successfully"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to move file: {str(e)}"
        }


def rename_file(old_path: str, new_path: str) -> dict:
    """Rename a file or move it to a new location.
    
    Args:
        old_path (str): Current file path
        new_path (str): New file path
    
    Returns:
        dict: status and message
    """
    try:
        os.rename(old_path, new_path)
        return {
            "status": "success",
            "old_path": old_path,
            "new_path": new_path,
            "message": "File renamed successfully"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to rename file: {str(e)}"
        }


def list_files(directory: str = ".", pattern: str = "*", recursive: bool = False) -> dict:
    """List files in a directory with optional pattern matching.
    
    Args:
        directory (str): Directory path (default: current directory)
        pattern (str): File pattern to match (default: "*" for all files)
        recursive (bool): Whether to search recursively (default: False)
    
    Returns:
        dict: status, files list, and directory info
    """
    try:
        path = Path(directory)
        
        if recursive:
            files = [str(f) for f in path.rglob(pattern) if f.is_file()]
        else:
            files = [str(f) for f in path.glob(pattern) if f.is_file()]
        
        return {
            "status": "success",
            "directory": str(path.absolute()),
            "pattern": pattern,
            "recursive": recursive,
            "file_count": len(files),
            "files": files
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to list files: {str(e)}"
        }


def list_directories(directory: str = ".", recursive: bool = False) -> dict:
    """List directories in a directory.
    
    Args:
        directory (str): Directory path (default: current directory)
        recursive (bool): Whether to search recursively (default: False)
    
    Returns:
        dict: status, directories list, and info
    """
    try:
        path = Path(directory)
        
        if recursive:
            dirs = [str(d) for d in path.rglob("*") if d.is_dir()]
        else:
            dirs = [str(d) for d in path.glob("*") if d.is_dir()]
        
        return {
            "status": "success",
            "directory": str(path.absolute()),
            "recursive": recursive,
            "directory_count": len(dirs),
            "directories": dirs
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to list directories: {str(e)}"
        }


def file_exists(file_path: str) -> dict:
    """Check if a file exists.
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        dict: status and existence status
    """
    try:
        exists = os.path.isfile(file_path)
        return {
            "status": "success",
            "file_path": file_path,
            "exists": exists
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to check file existence: {str(e)}"
        }


def directory_exists(dir_path: str) -> dict:
    """Check if a directory exists.
    
    Args:
        dir_path (str): Path to the directory
    
    Returns:
        dict: status and existence status
    """
    try:
        exists = os.path.isdir(dir_path)
        return {
            "status": "success",
            "directory_path": dir_path,
            "exists": exists
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to check directory existence: {str(e)}"
        }


def get_file_info(file_path: str) -> dict:
    """Get detailed information about a file.
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        dict: status and file information
    """
    try:
        if not os.path.exists(file_path):
            return {
                "status": "error",
                "message": f"File '{file_path}' does not exist"
            }
        
        stat_info = os.stat(file_path)
        path_obj = Path(file_path)
        
        return {
            "status": "success",
            "file_path": str(path_obj.absolute()),
            "file_name": path_obj.name,
            "file_extension": path_obj.suffix,
            "file_size": stat_info.st_size,
            "created_time": stat_info.st_ctime,
            "modified_time": stat_info.st_mtime,
            "accessed_time": stat_info.st_atime,
            "is_file": path_obj.is_file(),
            "is_directory": path_obj.is_dir()
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to get file info: {str(e)}"
        }


def delete_directory(dir_path: str, recursive: bool = False) -> dict:
    """Delete a directory.
    
    Args:
        dir_path (str): Path to the directory
        recursive (bool): If True, delete directory and all contents (default: False)
    
    Returns:
        dict: status and message
    """
    try:
        if not os.path.exists(dir_path):
            return {
                "status": "error",
                "message": f"Directory '{dir_path}' does not exist"
            }
        
        if recursive:
            shutil.rmtree(dir_path)
            message = "Directory and all contents deleted successfully"
        else:
            os.rmdir(dir_path)
            message = "Empty directory deleted successfully"
        
        return {
            "status": "success",
            "directory_path": dir_path,
            "message": message
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to delete directory: {str(e)}"
        }


def copy_directory(source: str, destination: str) -> dict:
    """Copy a directory from source to destination.
    
    Args:
        source (str): Source directory path
        destination (str): Destination directory path
    
    Returns:
        dict: status and message
    """
    try:
        shutil.copytree(source, destination)
        return {
            "status": "success",
            "source": source,
            "destination": destination,
            "message": "Directory copied successfully"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to copy directory: {str(e)}"
        }


def search_in_file(file_path: str, search_text: str, case_sensitive: bool = False) -> dict:
    """Search for text in a file and return matching lines.
    
    Args:
        file_path (str): Path to the file
        search_text (str): Text to search for
        case_sensitive (bool): Whether search should be case sensitive (default: False)
    
    Returns:
        dict: status, matches, and line numbers
    """
    try:
        matches = []
        with open(file_path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                if case_sensitive:
                    if search_text in line:
                        matches.append({"line_number": line_num, "content": line.strip()})
                else:
                    if search_text.lower() in line.lower():
                        matches.append({"line_number": line_num, "content": line.strip()})
        
        return {
            "status": "success",
            "file_path": file_path,
            "search_text": search_text,
            "match_count": len(matches),
            "matches": matches
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to search in file: {str(e)}"
        }


def get_file_lines(file_path: str, start_line: Optional[int] = None, end_line: Optional[int] = None) -> dict:
    """Get specific lines from a file.
    
    Args:
        file_path (str): Path to the file
        start_line (int): Starting line number (1-indexed, default: None for beginning)
        end_line (int): Ending line number (1-indexed, default: None for end)
    
    Returns:
        dict: status and lines
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            all_lines = f.readlines()
        
        total_lines = len(all_lines)
        start_idx = (start_line - 1) if start_line else 0
        end_idx = end_line if end_line else total_lines
        
        selected_lines = all_lines[start_idx:end_idx]
        
        return {
            "status": "success",
            "file_path": file_path,
            "total_lines": total_lines,
            "start_line": start_idx + 1,
            "end_line": min(end_idx, total_lines),
            "lines": [line.rstrip('\n') for line in selected_lines]
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to get file lines: {str(e)}"
        }


# Legacy function names for backward compatibility
delFile = delete_file
delFiles = delete_files
    
    

    