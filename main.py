import time
from STT import record_audio, transcribe
from LLM import LLM
from TTS import say

while True:
    record_audio()
    text = transcribe()
    print("📝 You said:", text)
    response = LLM(text)
    print("🤖 I said:", response)
    say(response)
    time.sleep(1)
