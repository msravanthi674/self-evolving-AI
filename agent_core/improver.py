import os
from dotenv import load_dotenv

try:
    from mistralai.client import MistralClient
except ImportError:
    from mistralai import Mistral as MistralClient

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")
client = MistralClient(api_key=api_key)

def run_improver(solution_text, feedback_text):
    """
    Improves a solution using evaluator feedback for refinement.
    """
    prompt = (
        f"Refine the solution using the feedback.\n\n"
        f"Solution:\n{solution_text}\n\nFeedback:\n{feedback_text}"
    )
    messages = [{"role": "user", "content": prompt}]

    if hasattr(client, "chat") and hasattr(client.chat, "complete"):
        response = client.chat.complete(model="mistral-small-latest", messages=messages)
    elif hasattr(client, "chat_complete"):
        response = client.chat_complete(model="mistral-small", messages=messages)
    else:
        response = client.chat(model="mistral-small", messages=messages)
    
    return response.choices[0].message.content
