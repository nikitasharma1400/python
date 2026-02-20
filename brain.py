from faster_whisper import WhisperModel
import os

def transcribe_file(file_path):
    if not os.path.exists(file_path):
        return "❌ Error: speech.wav not found. Run ear.py first!"

    print(f"--- 🧠 Ghost-Writer is analyzing your voice... ---")
    
    # 'base' is more accurate for laptop mics
    model = WhisperModel("base", device="cpu", compute_type="int8")

    segments, info = model.transcribe(file_path, beam_size=5)

    full_text = ""
    for segment in segments:
        full_text += segment.text + " "
    
    return full_text.strip()

if __name__ == "__main__":
    text = transcribe_file("speech.wav")
    
    if text:
        print(f"\n--- 📝 GHOST-WRITER READS: ---")
        print(f"> {text}\n")
    else:
        print("\n--- 🔇 The Ghost-Writer heard nothing. Try speaking louder! ---")