import whisper
import numpy as np
import os
import sys
import ctypes

# Add the path to the whisper library to the PATH environment variable
# This is a workaround for a known issue with the whisper library on Windows
# os.environ['PATH'] = os.environ['PATH'] + ';C:\\Users\\liorm\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\whisper'

model = whisper.load_model("base")

# Lazily-loaded Whisper model. It will only be created on the first call to
# ``transcribe_audio``. This avoids the heavy initialization cost when the
# module is imported but transcription is never used.
_model = None

def _get_model():
    """Return the Whisper model, loading it if necessary."""
    global _model
    if _model is None:
        _model = whisper.load_model("base")
    return _model

def transcribe_audio(audio_data, sample_rate=16000):
    """Transcribe ``audio_data`` using a lazily loaded Whisper model."""
    audio_data = audio_data.flatten()
    model = _get_model()
    result = model.transcribe(audio_data, fp16=False, language='en')
    return result["text"]