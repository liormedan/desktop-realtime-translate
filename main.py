import sys
import threading
import time
import queue
import numpy as np
import whisper
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from audio.audio_capture import start_stream

# טען את מודל Whisper
model = whisper.load_model("base")  # אפשר גם tiny / small / medium

# אתחול GUI
app = QApplication(sys.argv)
window = MainWindow()
window.show()

# משתנים גלובליים
stream = None
audio_q = None
volume_q = queue.Queue()
running = False

def update_volume():
    while running:
        try:
            volume = volume_q.get(timeout=1)
            level = min(int(volume * 10), 100)
            window.progress.setValue(level)
        except queue.Empty:
            pass
        time.sleep(0.05)

def recognize_loop():
    buffer = []
    sample_rate = 16000
    chunk_duration = 5  # שניות
    chunk_size = int(sample_rate * chunk_duration)

    while running:
        try:
            data = audio_q.get(timeout=1)
            if isinstance(data, np.ndarray):
                buffer.extend(data[:, 0])

                if len(buffer) >= chunk_size:
                    audio_np = np.array(buffer[:chunk_size])
                    buffer = buffer[chunk_size:]

                    print("🔎 מזהה טקסט...")
                    result = model.transcribe(audio_np, language="he", fp16=False)
                    text = result.get("text", "").strip()
                    if text:
                        window.text_area.append(text)

        except Exception as e:
            print(f"שגיאת זיהוי: {e}")
        time.sleep(0.1)

def callback(indata, frames, time_, status):
    volume = np.linalg.norm(indata)
    volume_q.put(volume)
    audio_q.put(indata.copy())

def toggle_start():
    global stream, audio_q, running
    if not running:
        print("🎙️ מתחיל להאזין ולזהות דיבור...")
        audio_q = queue.Queue()
        device = None  # אפשר להחליף לפי צורך
        stream, _ = start_stream(device=device, callback=callback)
        running = True
        threading.Thread(target=update_volume, daemon=True).start()
        threading.Thread(target=recognize_loop, daemon=True).start()

def toggle_stop():
    global stream, running
    if stream:
        print("🛑 עצירה.")
        stream.stop()
        stream.close()
        running = False
        window.progress.setValue(0)

# חיבור כפתורים
window.start_button.clicked.connect(toggle_start)
window.stop_button.clicked.connect(toggle_stop)

sys.exit(app.exec_())
