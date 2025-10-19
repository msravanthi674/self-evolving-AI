from mistralai.client import MistralClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
mistral_api_key = os.getenv("MISTRAL_API_KEY")

# Initialize Mistral client
client = MistralClient(api_key=mistral_api_key)

def run_evaluator(solution_text):
    """
    Evaluator agent reviews the generated solution and provides structured feedback
    with a quality score (0–10).
    """
    prompt = (
        "Evaluate the following solution and provide detailed feedback and a score (0–10):\n\n"
        f"Solution:\n{solution_text}"
    )
    messages = [{"role": "user", "content": prompt}]
    chat_response = client.chat.complete(
        model="mistral-small-latest",
        messages=messages
    )
    return chat_response.choices[0].message.content
