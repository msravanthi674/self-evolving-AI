from mistralai import Mistral
import os
from dotenv import load_dotenv

load_dotenv()
mistral_api_key = os.getenv("MISTRAL_API_KEY")
client = Mistral(api_key=mistral_api_key)

def run_evaluator(solution_text):
    prompt = (
        "Review the following solution and provide constructive feedback "
        "and a score (0-10):\nSolution:\n" + solution_text
    )
    messages = [{"role": "user", "content": prompt}]
    chat_response = client.chat(
        model="mistral-small",
        messages=messages
    )
    return chat_response.choices[0].message.content
