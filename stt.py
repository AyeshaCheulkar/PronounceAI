import whisper
import os
import re

# Use 'base' for faster performance, 'medium' for higher accuracy
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    if not os.path.exists(audio_path):
        return ""
    
    result = model.transcribe(audio_path, language="en")
    text = result["text"].strip().lower()
    
    # Remove punctuation
    clean_text = re.sub(r'[^\w\s]', '', text)
    return clean_text