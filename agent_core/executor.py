from mistralai import Mistral
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

# Initialize new SDK client
client = Mistral(api_key=api_key)

def run_executor(task_prompt):
    """
    Executor agent that generates an initial solution 
    using Mistral's latest chat completion API.
    """
    chat_response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {"role": "user", "content": task_prompt}
        ]
    )
    return chat_response.choices[0].message.content
