from mistralai.client import MistralClient
import os
from dotenv import load_dotenv

load_dotenv()
mistral_api_key = os.getenv("MISTRAL_API_KEY")
client = MistralClient(api_key=mistral_api_key)

def run_evaluator(solution_text):
    prompt = f"Review the following solution and provide constructive feedback and a score (0-10):\nSolution:\n{solution_text}"
    messages = [{"role": "user", "content": prompt}]
    chat_response = client.chat.complete(
        model="mistral-small-latest",
        messages=messages
    )
    return chat_response.choices[0].message.content
