"""
url: https://docs.langchain.com/oss/python/langchain/quickstart
"""

import os
from langchain.agents.factory import create_agent
from dotenv import load_dotenv
load_dotenv()

MODEL = "gpt-5-nano"

# Tool
def get_weather(city: str) -> str:
    """Get weather for a given city"""
    return f"It's always sunny in {city}"


# Agent
agent = create_agent(
    model=MODEL,
    tools=[get_weather],
    system_prompt="You are an AI assistant",
)

# Execute the Agent
user_question = "What is the weather like in Atlanta"
response = agent.invoke({"messages": [("user", user_question)]})
print("User question => {}".format(user_question))

