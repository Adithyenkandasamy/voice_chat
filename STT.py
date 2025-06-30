import whisper
import pyaudio
import wave

# Config
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

# Load Whisper model once
model = whisper.load_model("base")  # or "tiny", "small", etc.

def record_audio():
    print("🎤 Listening...")

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        frames.append(stream.read(CHUNK))

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def transcribe():
    result = model.transcribe(WAVE_OUTPUT_FILENAME)
    return result['text']

if __name__ == "__main__":
    record_audio()
    text = transcribe()
    print("📝 You said:", text)
