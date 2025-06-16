from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QHBoxLayout
)
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("🔊 תרגום בזמן אמת")
        self.resize(600, 300)

        # צבע רקע כחול
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#d0e7ff"))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # פריסה ראשית
        self.layout = QVBoxLayout()

        # תווית תרגום
        self.label = QLabel("...")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 14))
        self.layout.addWidget(self.label)

        # אזור בקרה
        controls = QHBoxLayout()

        # כפתור התחלה
        self.start_button = QPushButton("▶️ התחלת תרגום")
        controls.addWidget(self.start_button)

        # כפתור עצירה
        self.stop_button = QPushButton("⏸️ עצור")
        controls.addWidget(self.stop_button)

        # בחירת שפה
        self.language_selector = QComboBox()
        self.language_selector.addItems(["עברית", "אנגלית", "צרפתית", "רוסית", "ערבית"])
        controls.addWidget(self.language_selector)

        self.layout.addLayout(controls)

        self.setLayout(self.layout)

    def update_text(self, text):
        self.label.setText(text)

    def get_selected_language_code(self):
        name = self.language_selector.currentText()
        return {
            "עברית": "iw",
            "אנגלית": "en",
            "צרפתית": "fr",
            "רוסית": "ru",
            "ערבית": "ar",
        }.get(name, "iw")
