from google.adk.agents import Agent
from .weather_utils import get_weather, get_current_time
from .file_ops import *


root_agent = Agent(
    name="pro_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the time and weather in a city. You can make file operations based on user queries."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city. You can make file operations based on user queries."
    ),
    tools=[get_weather, get_current_time,get_cwd,mkdir,chdir,create_file],
)