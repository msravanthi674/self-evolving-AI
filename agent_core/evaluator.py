import os
from dotenv import load_dotenv

try:
    from mistralai.client import MistralClient
except ImportError:
    from mistralai import Mistral as MistralClient

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")
client = MistralClient(api_key=api_key)

def run_evaluator(solution_text):
    """
    Evaluates a generated solution and provides feedback with a score.
    """
    prompt = f"Provide constructive feedback and a score (0–10) for the following solution:\n{solution_text}"
    messages = [{"role": "user", "content": prompt}]

    if hasattr(client, "chat") and hasattr(client.chat, "complete"):
        response = client.chat.complete(model="mistral-small-latest", messages=messages)
    elif hasattr(client, "chat_complete"):
        response = client.chat_complete(model="mistral-small", messages=messages)
    else:
        response = client.chat(model="mistral-small", messages=messages)
    
    return response.choices[0].message.content
