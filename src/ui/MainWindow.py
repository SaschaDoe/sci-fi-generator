from PySide6.QtWidgets import QMainWindow, QApplication, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sci-Fi Generator")

        screen = QApplication.primaryScreen().availableGeometry()
        width = int(screen.width() * 0.9)
        height = int(screen.height() * 0.9)
        x = int(screen.width() / 2 - width / 2)
        y = int(screen.height() / 2 - height / 2)

        self.setGeometry(x,y,width,height)

        self.label = QLabel("Hello World!", self)
        self.label.setGeometry(width // 2 - 50, height // 2 - 15, 200, 30)
