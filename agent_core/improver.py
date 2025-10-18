from mistralai import Mistral # type: ignore
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()
mistral_api_key = os.getenv("MISTRAL_API_KEY")

def run_improver(solution_text, feedback_text):
    """
    Improver agent refines the provided solution based on evaluator feedback.
    """
    client = Mistral(api_key=mistral_api_key)
    
    prompt = (f"Improve the following solution using the evaluator's feedback:\nSolution:\n{solution_text}\n"
              f"Feedback:\n{feedback_text}")
    
    chat_response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    return chat_response.choices[0].message.content
