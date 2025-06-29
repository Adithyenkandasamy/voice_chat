from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def LLM(prompt):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "NULL",
            "X-Title": "NULL",
        },
        model="deepseek/deepseek-r1:free",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a smart and casual voice assistant. "
                    "Speak like a human — respond in 1–2 short sentences. "
                    "Keep it simple, natural, and friendly like real conversation. "
                    "If the user says 'hi', just say 'Hi!' or 'Hello!' — "
                    "don't explain anything unless asked directly."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    response = completion.choices[0].message.content
    return response.replace("\n", " ").strip()

if __name__ == "__main__":
    print(LLM("Hi"))
