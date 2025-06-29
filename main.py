import pyaudio
import wave
import sys
import time
import LLM
import respond

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=chunk)

while True:
    try:
        # Initialize PyAudio
        p = pyaudio.PyAudio()
        
        # Open stream
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=chunk)

        print("* recording")
        frames = []

        for i in range(0, int(RATE / chunk * RECORD_SECONDS)):
            data = stream.read(chunk)
            frames.append(data)

        print("* done recording")

        # Stop and close stream
        stream.stop_stream()
        stream.close()

        # Save audio to file
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        # Process with LLM and respond
        text = LLM.LLM(WAVE_OUTPUT_FILENAME)
        respond.say(text)
        
        # Terminate PyAudio
        p.terminate()
        
        time.sleep(1)
    
    except Exception as e:
        print(f"Error: {str(e)}")
        time.sleep(1)
