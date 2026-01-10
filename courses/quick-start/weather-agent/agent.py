"""
url: https://docs.langchain.com/oss/python/langchain/quickstart
"""

import os
from langchain.agents.factory import create_agent
from dotenv import load_dotenv
load_dotenv()

MODEL = "gpt-5-nano"

# Tools
def get_weather(city: str) -> str:
    """Get weather for a given city"""
    return f"It's always sunny in {city}"

def add_two_numbers(num1: int, num2: int) -> int:
    """Add two numbers"""
    return num1 + num2

# Agent
agent = create_agent(
    model=MODEL,
    tools=[get_weather, add_two_numbers],
    system_prompt="You are an AI assistant",
)

# Execute the Agent
user_question = ("What is two plus two?")
response = agent.invoke({"messages": [("user", user_question)]})
messages = response['messages']
for i in messages:
    print(i)
