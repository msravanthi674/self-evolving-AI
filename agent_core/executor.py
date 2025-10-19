import os
from dotenv import load_dotenv

# Try to import both old & new clients safely
try:
    from mistralai.client import MistralClient  # New SDK (v1+)
except ImportError:
    from mistralai import Mistral as MistralClient  # Old SDK fallback

# Load environment variables
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

client = MistralClient(api_key=api_key)

def run_executor(task_prompt):
    """
    Executor generates an initial solution from a user-defined task prompt.
    """
    messages = [{"role": "user", "content": task_prompt}]
    
    # Handle version differences in method call
    if hasattr(client, "chat") and hasattr(client.chat, "complete"):
        chat_response = client.chat.complete(model="mistral-small-latest", messages=messages)
    elif hasattr(client, "chat_complete"):
        chat_response = client.chat_complete(model="mistral-small", messages=messages)
    elif hasattr(client, "chat"):
        chat_response = client.chat(model="mistral-small", messages=messages)
    else:
        raise AttributeError("No chat-compatible method available in mistralai client.")
        
    return chat_response.choices[0].message.content
