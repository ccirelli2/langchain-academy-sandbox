"""
Create a weather agent
https://docs.langchain.com/oss/python/langchain/overview
"""
import os
import logging
from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent
load_dotenv()

# Settings
logging.basicConfig(level=logging.INFO)

# Create a Tool & Define Metadata
@tool(
    name_or_callable="weather lookup",
    description="Look up weather for a US city"
)
def get_weather(city: str) -> str:
    return f"The weather for {city} is shitty"

# Create Agent
agent = create_agent(
    model="gpt-5-nano",
    tools=[get_weather],
    system_prompt="You are a helpful AI assistant"
)

