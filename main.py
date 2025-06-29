import pyaudio
import wave
import sys
import time
import LLM
import respond

# Configuration
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "output.wav"

# Initialize PyAudio
p = pyaudio.PyAudio()

# Function to get available audio devices
def list_audio_devices():
    print("Available audio devices:")
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        print(f"Device {i}: {device_info['name']}")

# Function to process audio
def process_audio():
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    print("* Recording for 3 seconds...")
    frames = []
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    print("* Done recording")
    
    stream.stop_stream()
    stream.close()
    
    # Save the recording
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    try:
        # Process with LLM
        text = LLM.LLM(WAVE_OUTPUT_FILENAME)
        print(f"Assistant: {text}")
        respond.say(text)
    except Exception as e:
        print(f"Error processing audio: {str(e)}")

# Main loop
if __name__ == "__main__":
    try:
        # List available audio devices
        list_audio_devices()
        
        print("\nVoice Assistant is ready!")
        print("Press Ctrl+C to stop")
        
        while True:
            # input("\nPress Enter to start recording...")
            process_audio()
            
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        p.terminate()
