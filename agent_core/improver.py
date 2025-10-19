from mistralai.client import MistralClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
mistral_api_key = os.getenv("MISTRAL_API_KEY")

# Initialize Mistral client
client = MistralClient(api_key=mistral_api_key)

def run_improver(solution_text, feedback_text):
    """
    Improver agent enhances the original solution using evaluator feedback.
    """
    prompt = (
        "Improve the following solution according to the evaluator's feedback.\n\n"
        f"Solution:\n{solution_text}\n\n"
        f"Feedback:\n{feedback_text}"
    )
    messages = [{"role": "user", "content": prompt}]
    chat_response = client.chat.complete(
        model="mistral-small-latest",
        messages=messages
    )
    return chat_response.choices[0].message.content
