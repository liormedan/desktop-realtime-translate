import pytest
from PyQt5.QtWidgets import QApplication

from ui.main_window import MainWindow


def test_main_window_initializes():
    app = QApplication.instance() or QApplication([])
    window = MainWindow()
    assert isinstance(window, MainWindow)
    window.close()
    # only quit app if we created it
    if not QApplication.instance().topLevelWidgets():
        app.quit()