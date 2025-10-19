from mistralai.client import MistralClient

import os
from dotenv import load_dotenv

load_dotenv()
mistral_api_key = os.getenv("MISTRAL_API_KEY")
client = Mistral(api_key=mistral_api_key)

def run_executor(task_prompt):
    messages = [{"role": "user", "content": task_prompt}]
    chat_response = client.chat(
        model="mistral-small",
        messages=messages
    )
    return chat_response.choices[0].message.content


