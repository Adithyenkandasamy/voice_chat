# Install with: pip install assemblyai pyaudio wave

import pyaudio
import wave
import assemblyai as aai
from LLM import LLM
from respond import say

# ========== AssemblyAI API Setup ==========
aai.settings.api_key = "d1b8efd7443140b88901113738f8c44a"
transcriber = aai.Transcriber()

# ========== Audio Recording Config ==========
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

# ========== Function: Record Microphone Audio ==========
def record_audio():
    print("🎤 Speak now...")

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print("✅ Recording saved.")

# ========== Function: Transcribe Using AssemblyAI ==========
def transcribe_audio():
    print("🧠 Transcribing...")

    transcript = transcriber.transcribe(WAVE_OUTPUT_FILENAME)

    if transcript.status == "error":
        raise RuntimeError(f"Transcription failed: {transcript.error}")

    print(f"\n🗣️ Transcription:\n{transcript.text}\n")
    return transcript.text

# ========== Main ==========
if __name__ == "__main__":
    try:
        record_audio()
        text = transcribe_audio()
        # ========== SPACE FOR LLM ==========
        llm_reply = LLM(text)
        print(f"🤖 LLM: {llm_reply}")

        # ========== SPACE FOR TTS ==========
        say(llm_reply)

    except KeyboardInterrupt:
        print("\n❌ Interrupted by user.")
    except Exception as e:
        print(f"❌ Error: {e}")
