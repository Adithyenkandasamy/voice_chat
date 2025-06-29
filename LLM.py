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
            "HTTP-Referer": "NULL", # Optional. Site URL for rankings on openrouter.ai.
            "X-Title": "NULL", # Optional. Site title for rankings on openrouter.ai.
        },
        model="deepseek/deepseek-r1:free",
        messages=[
            {
                "role": "user",
                "content": prompt+"it is anvoice bot so giv any answers in a short and simple way and also without emojis and special symbols"  
            }
        ]
    )

    return completion.choices[0].message.content

if __name__ == "__main__":
    print(LLM("Hello, how are you?"))
    