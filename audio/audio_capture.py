import sounddevice as sd
import numpy as np
import queue

q = queue.Queue()

def callback(indata, frames, time, status):
    volume = np.linalg.norm(indata)
    q.put(volume)

def start_stream(sample_rate=16000, channels=1, device=None):
    stream = sd.InputStream(
        callback=callback,
        channels=channels,
        samplerate=sample_rate,
        device=device
    )
    stream.start()
    return stream, q
