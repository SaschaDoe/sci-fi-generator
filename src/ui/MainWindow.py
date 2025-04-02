from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from ui.components.button.sci_fi_button import SciFiButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sci-Fi Generator")

        screen = QApplication.primaryScreen().availableGeometry()
        width = int(screen.width() * 0.9)
        height = int(screen.height() * 0.9)
        x = int(screen.width() / 2 - width / 2)
        y = int(screen.height() / 2 - height / 2)
        self.setGeometry(x, y, width, height)

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create vertical layout
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)  # Center items in layout

        # Add label
        self.label = QLabel("Sci-Fi Generator")
        layout.addWidget(self.label, alignment=Qt.AlignCenter)

        # Add spacing below label
        layout.addSpacing(40)

        # Add NEW button
        self.newButton = SciFiButton.New("New")
        self.newButton.setFixedSize(200, 40)  # Fixed size
        layout.addWidget(self.newButton, alignment=Qt.AlignCenter)

        # Add spacing between buttons
        layout.addSpacing(20)

        # Add EXIT button below the NEW button
        self.exitButton = SciFiButton.Exit("Exit")
        self.exitButton.setFixedSize(200, 40)  # Fixed size
        layout.addWidget(self.exitButton, alignment=Qt.AlignCenter)
        self.exitButton.clicked.connect(self.close)