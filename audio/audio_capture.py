import sounddevice as sd

def start_stream(sample_rate=16000, channels=1, device=None, callback=None):
    stream = sd.InputStream(
        callback=callback,
        channels=channels,
        samplerate=sample_rate,
        device=device
    )
    stream.start()
    return stream, None
