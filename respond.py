import requests
import os
import tempfile

def say(text):
    url = "http://localhost:8880/v1/audio/speech"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "input": text,
        "voice": "af_alloy"  # Use the voice that your server actually loaded
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            f.write(response.content)
            temp_audio_path = f.name
        os.system(f"mpg123 {temp_audio_path}")  # Optional: replace with ffplay for better support
        os.remove(temp_audio_path)
    else:
        print("TTS request failed:", response.status_code, response.text)

if __name__ == "__main__":
    say("hello hi tell me about yourself")
