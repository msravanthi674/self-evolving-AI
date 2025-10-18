from mistralai import Mistral # type: ignore
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()
mistral_api_key = os.getenv("MISTRAL_API_KEY")

def run_executor(task_prompt):
    """
    Executor agent generates initial solution based on task prompt.
    """
    client = Mistral(api_key=mistral_api_key)
    
    chat_response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {
                "role": "user",
                "content": task_prompt
            }
        ]
    )
    
    return chat_response.choices[0].message.content
