from mistralai import Mistral
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

client = Mistral(api_key=api_key)

def run_improver(solution_text, feedback_text):
    """
    Improver agent that enhances the original solution 
    based on evaluator feedback and suggestions.
    """
    improve_prompt = (
        f"Based on the evaluator's feedback below, improve the following solution.\n\n"
        f"Solution:\n{solution_text}\n\n"
        f"Feedback:\n{feedback_text}"
    )

    chat_response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {"role": "user", "content": improve_prompt}
        ]
    )
    return chat_response.choices[0].message.content
