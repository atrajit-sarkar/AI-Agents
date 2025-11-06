from google.adk.agents import Agent
import system_tools


system_agent = Agent(
    name="telegram_system_agent",
    model="gemini-2.0-flash",
    description=(
        "An intelligent system control agent that can perform comprehensive file operations, "
        "directory management, command execution, file encryption/decryption, screen capture, "
        "and various system-level tasks. This agent provides remote system control capabilities "
        "through natural language interaction."
    ),
    instruction=(
        "You are a powerful system control agent with extensive capabilities. "
        "When a user gives you a query, analyze what needs to be done and execute the appropriate tools. "
        "Always provide clear feedback about what actions were taken. "
        "For complex operations involving multiple steps, execute them in the correct order. "
        "If a tool returns an error, explain the issue to the user clearly. "
        "Always confirm successful completion of tasks with the user. "
        "When working with file paths, ensure they are valid and exist before performing operations. "
        "Be cautious with destructive operations like delete, encrypt, or execute commands. "
        "For screen recording, suggest reasonable durations (5-30 seconds) to avoid huge file sizes."
    ),
    tools=[
        # Directory operations
        system_tools.get_cwd,
        system_tools.chdir,
        system_tools.list_directory,
        system_tools.create_directory,
        system_tools.delete_directory,
        
        # File operations
        system_tools.create_file,
        system_tools.read_file,
        system_tools.write_file,
        system_tools.delete_file,
        system_tools.copy_file,
        system_tools.move_file,
        system_tools.file_exists,
        system_tools.get_file_info,
        system_tools.batch_rename_files,
        
        # System operations
        system_tools.execute_command,
        system_tools.change_file_permissions,
        
        # Security operations
        system_tools.encrypt_files,
        system_tools.decrypt_files,
        
        # Screen operations
        system_tools.capture_screenshot,
        system_tools.record_screen,
    ],
)
