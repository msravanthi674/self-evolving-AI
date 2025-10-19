from mistralai import Mistral
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

client = Mistral(api_key=api_key)

def run_evaluator(solution_text):
    """
    Evaluator agent that reviews a solution and gives feedback with a numeric score.
    """
    feedback_prompt = (
        f"Evaluate the following solution for quality, correctness, "
        f"and clarity. Give actionable feedback and a score out of 10.\n\n"
        f"Solution:\n{solution_text}"
    )

    chat_response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {"role": "user", "content": feedback_prompt}
        ]
    )
    return chat_response.choices[0].message.content
