import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_cancer_support_response(user_input: str) -> str:
    system_prompt = (
        "You are a compassionate assistant specialized in supporting cancer patients. "
        "Respond empathetically, provide clear information about cancer, its treatments, symptoms, "
        "and coping strategies."
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content.strip()