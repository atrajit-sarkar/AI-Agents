from google.adk.agents import Agent
from .weather_utils import get_weather, get_current_time
from .file_ops import *


root_agent = Agent(
    name="pro_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the time and weather in a city. You can make comprehensive file operations based on user queries."
    ),
    instruction=(
        "When user give you a query count the number of tools needed for that query to resolve sucessfully. If you get the exact number of success message from the tools returns then only send the user final reply unless wait to get all the success messages."
    ),
    tools=[
        # Weather & Time tools
        get_weather, 
        get_current_time,
        
        # Directory operations
        get_cwd, 
        mkdir, 
        chdir,
        list_directories,
        directory_exists,
        delete_directory,
        copy_directory,
        
        # File creation & writing
        create_file,
        write_file,
        
        # File reading
        read_file,
        get_file_lines,
        search_in_file,
        
        # File operations
        copy_file,
        move_file,
        rename_file,
        delete_file,
        delete_files,
        
        # File information
        file_exists,
        get_file_info,
        list_files,
    ],
)