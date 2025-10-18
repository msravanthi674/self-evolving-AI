from mistralai import Mistral # type: ignore
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()
mistral_api_key = os.getenv("MISTRAL_API_KEY")

def run_evaluator(solution_text):
    """
    Evaluator agent reviews solution and returns feedback + score.
    """
    client = Mistral(api_key=mistral_api_key)
    
    prompt = f"Review the following solution and provide constructive feedback and a score (0-10):\nSolution:\n{solution_text}"
    
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
