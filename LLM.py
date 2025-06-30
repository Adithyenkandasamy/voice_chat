import requests

def ask_ollama(prompt, model="mistral"):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model,
        "prompt": prompt+"""You are a voice assistant named Jarvis. Speak clearly and briefly.
        Use simple, correct language. Limit replies to under 20 words. No small talk or extra details.""",
        "stream": True
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["response"]

# Example usage
# ask_ollama("What's the capital of France?")
