import sys
import threading
import time
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from audio.audio_capture import start_stream

app = QApplication(sys.argv)
window = MainWindow()
window.show()

stream = None
q = None
running = False

def update_volume():
    while running:
        try:
            volume = q.get(timeout=1)
            level = min(int(volume * 10), 100)
            window.progress.setValue(level)
        except:
            pass
        time.sleep(0.05)

def toggle_start():
    global stream, q, running
    if not running:
        device = None  # שים כאן index או שם של VB-Cable אם אתה יודע
        stream, q = start_stream(device=device)
        running = True
        threading.Thread(target=update_volume, daemon=True).start()

def toggle_stop():
    global stream, running
    if stream:
        stream.stop()
        stream.close()
        running = False
        window.progress.setValue(0)

window.start_button.clicked.connect(toggle_start)
window.stop_button.clicked.connect(toggle_stop)

sys.exit(app.exec_())
