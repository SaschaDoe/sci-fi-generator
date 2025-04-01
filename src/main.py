import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QLabel
from src.ui.MainWindow import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    return window, app

if __name__ == "__main__":
    window, app = main()
    sys.exit(app.exec())