import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)
response = client.responses.create(
    model="gpt-5-nano",
    instructions="You are an expert at telling dad jokes",
    input="Write a short dad joke."
)

print("LLM Response")
print(response.output_text)


