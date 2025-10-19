from mistralai.client import MistralClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
mistral_api_key = os.getenv("MISTRAL_API_KEY")

# Initialize Mistral client
client = MistralClient(api_key=mistral_api_key)

def run_executor(task_prompt):
    """
    Executor agent generates an initial solution based on the provided task description.
    """
    messages = [{"role": "user", "content": task_prompt}]
    chat_response = client.chat.complete(
        model="mistral-small-latest",
        messages=messages
    )
    return chat_response.choices[0].message.content
