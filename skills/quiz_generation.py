from dotenv import load_dotenv
import os
import json
from google import genai

load_dotenv()
client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

def generate_quiz(subject: str, topic: str, difficulty: str, num_questions: int = 3):
    prompt = f"""
    Create {num_questions} multiple-choice quiz questions.
    Subject: {subject}
    Topic: {topic}
    Difficulty: {difficulty}

    Return only valid JSON.
    Do not wrap the response in wrapper.
    Do not use code fences.

    Format:

    [
        {{
            "question": "...",
            "options": {{
                "A": "...",
                "B": "...",
                "C": "...",
                "D": "..."
            }},
            "answer": "A"
        }}
    ]
    """

    response = client.models.generate_content(
        model = "gemini-2.5-flash", contents = prompt
    )
    # print(response.text)

    cleaned_text = response.text.strip()
    cleaned_text = cleaned_text.replace("```json", "")
    cleaned_text = cleaned_text.replace("```", "")
    cleaned_text = cleaned_text.strip()
    return json.loads(cleaned_text)
