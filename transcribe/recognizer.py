import whisper
import numpy as np
import os
import sys
import ctypes

# Add the path to the whisper library to the PATH environment variable
# This is a workaround for a known issue with the whisper library on Windows
# os.environ['PATH'] = os.environ['PATH'] + ';C:\\Users\\liorm\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\whisper'

model = whisper.load_model("base")

def transcribe_audio(audio_data, sample_rate=16000):
    audio_data = audio_data.flatten()
    result = model.transcribe(audio_data, fp16=False, language='en')
    return result["text"]
