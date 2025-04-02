from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from ui.components.button.sci_fi_button import SciFiButton
from ui.components.screens.BaseScreen import BaseScreen
from ui.navigation.ScreenType import ScreenType
from ui.navigation.mediator import INavigationMediator


class MainMenuScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        self.mediator = None
        self._setup_ui()

    @property
    def screen_type(self) -> ScreenType:
        return ScreenType.MAIN_MENU

    def set_mediator(self, mediator: INavigationMediator):
        self.mediator = mediator

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add label
        self.label = QLabel("Sci-Fi Generator")
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Add spacing below label
        layout.addSpacing(40)

        # Add NEW button
        self.newButton = SciFiButton.Normal("New")
        self.newButton.setFixedSize(200, 40)
        layout.addWidget(self.newButton, alignment=Qt.AlignmentFlag.AlignCenter)

        # Connect NEW button to request navigation via mediator
        self.newButton.clicked.connect(self._on_new_clicked)

        # Add spacing between buttons
        layout.addSpacing(20)

        # Add EXIT button below the NEW button
        self.exitButton = SciFiButton.Exit("Exit")
        self.exitButton.setFixedSize(200, 40)
        layout.addWidget(self.exitButton, alignment=Qt.AlignmentFlag.AlignCenter)

        # Connect EXIT button to request exit via mediator
        self.exitButton.clicked.connect(self._on_exit_clicked)

    def _on_new_clicked(self):
        if self.mediator:
            self.mediator.navigate_to(ScreenType.CIVILIZATION)

    def _on_exit_clicked(self):
        if self.mediator:
            self.mediator.exit_application()