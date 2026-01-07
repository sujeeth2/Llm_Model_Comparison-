from openai import OpenAI
import os

def chatgpt_response(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "OPENAI_API_KEY not found"

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    return response.output_text
