import requests
import os
import tempfile

def say(text):
    url = "https://f5cb-34-169-64-158.ngrok-free.app/speak"
    
    payload = {
        "text": text
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            f.write(response.content)
            temp_audio_path = f.name
        
        print(f"🔊 Playing audio: {temp_audio_path}")
        os.system(f"ffplay -autoexit -nodisp {temp_audio_path}")  # <-- safer player
        os.remove(temp_audio_path)
    else:
        print("❌ TTS request failed:", response.status_code, response.text)

# Run test
# say("Hello! I hope you're having a great day. Please let me know if there's anything I can do to assist you with your questions, tasks, or daily goals.")



