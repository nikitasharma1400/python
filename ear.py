import wave
import struct
from pvrecorder import PvRecorder

def record_and_transcribe():
    # SET TO INDEX 1 based on your mic check!
    recorder = PvRecorder(device_index=1, frame_length=512) 
    audio = []

    print("\n--- 🎙️ GHOST-WRITER IS LISTENING... ---")
    print("--- Speak into your laptop mic, then press Ctrl+C ---")
    
    try:
        recorder.start()
        while True:
            frame = recorder.read()
            audio.extend(frame)
    except KeyboardInterrupt:
        recorder.stop()
        print("\n--- ✅ Recording stopped. Saving audio... ---")
        
        # Save as speech.wav
        with wave.open("speech.wav", 'w') as f:
            f.setparams((1, 2, 16000, 512, "NONE", "not compressed"))
            f.writeframes(struct.pack("h" * len(audio), *audio))
        
        print("--- 📝 File saved! Ready for brain.py ---")
    finally:
        recorder.delete()

if __name__ == "__main__":
    record_and_transcribe()