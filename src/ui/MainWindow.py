from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QStackedWidget
from ui.components.screens import BaseScreen
from ui.components.screens.civilisation_generation_screen import CivilizationScreen
from ui.components.screens.main_menu_screen import MainMenuScreen
from ui.navigation.ScreenType import ScreenType
from ui.navigation.mediator import NavigationMediator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sci-Fi Generator")
        self._setup_window_geometry()
        self._setup_widget_structure()

        self.mediator = NavigationMediator(main_window=self, close_callback=self.close)

        self._setup_screens()

        self.mediator.navigate_to(ScreenType.MAIN_MENU)

    def _setup_window_geometry(self):
        """Configure the window size and position"""
        screen = QApplication.primaryScreen().availableGeometry()
        width = int(screen.width() * 0.9)
        height = int(screen.height() * 0.9)
        x = int(screen.width() / 2 - width / 2)
        y = int(screen.height() / 2 - height / 2)
        self.setGeometry(x, y, width, height)

    def _setup_widget_structure(self):
        """Create widget stack"""
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.stacked_widget = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widget)

    def _setup_screens(self):
        """Create all screen widgets and register them with the mediator"""
        self._setup_screen(MainMenuScreen())
        self._setup_screen(CivilizationScreen())

    def _setup_screen(self, screen: BaseScreen):
        screen.set_mediator(self.mediator)
        self.stacked_widget.addWidget(screen)
        self.mediator.register_screen(screen.screen_type, screen)