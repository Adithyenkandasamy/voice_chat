import time
from STT import record_audio, transcribe
from LLM import ask_ollama
from TTS import say

while True:
    record_audio()
    text = transcribe()
    print("📝 You said:", text)
    response = ask_ollama(text)
    print("🤖 I said:", response)
    say(response)
    time.sleep(1)
