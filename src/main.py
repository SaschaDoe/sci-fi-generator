import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QLabel

from ui.MainWindow import MainWindow


def main():
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    window = MainWindow()
    window.show()

    return window, app

if __name__ == "__main__":
    window, app = main()
    sys.exit(app.exec())