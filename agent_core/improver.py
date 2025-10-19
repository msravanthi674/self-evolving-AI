from mistralai.client import MistralClient

import os
from dotenv import load_dotenv

load_dotenv()
mistral_api_key = os.getenv("MISTRAL_API_KEY")
client = Mistral(api_key=mistral_api_key)

def run_improver(solution_text, feedback_text):
    prompt = (
        "Improve the following solution using the evaluator's feedback:\n"
        f"Solution:\n{solution_text}\nFeedback:\n{feedback_text}"
    )
    messages = [{"role": "user", "content": prompt}]
    chat_response = client.chat(
        model="mistral-small",
        messages=messages
    )
    return chat_response.choices[0].message.content


