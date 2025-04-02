from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QComboBox, QLineEdit, QFormLayout, QLabel, QWidget

from ui.components.button.sci_fi_button import SciFiButton

from ui.components.screens.BaseScreen import BaseScreen
from ui.navigation.ScreenType import ScreenType
from ui.navigation.mediator import INavigationMediator


class CivilizationScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        self.mediator = None
        self._setup_ui()

    @property
    def screen_type(self) -> ScreenType:
        return ScreenType.CIVILIZATION

    def set_mediator(self, mediator: INavigationMediator):
        self.mediator = mediator

    def _setup_ui(self):
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Title
        title_label = QLabel("Civilization Generator")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        # Add spacing
        main_layout.addSpacing(20)

        # Form layout for inputs
        form_layout = QFormLayout()
        main_layout.addLayout(form_layout)

        # Name input
        self.name_input = QLineEdit()
        form_layout.addRow("Civilization Name:", self.name_input)

        # Technology level
        self.tech_level = QComboBox()
        self.tech_level.addItems(["Primitive", "Industrial", "Modern", "Advanced", "Futuristic", "Post-Singularity"])
        form_layout.addRow("Technology Level:", self.tech_level)

        # Social structure
        self.social_structure = QComboBox()
        self.social_structure.addItems(["Tribal", "Feudal", "Democracy", "Republic", "Technocracy", "Hive Mind"])
        form_layout.addRow("Social Structure:", self.social_structure)

        # Environment
        self.environment = QComboBox()
        self.environment.addItems(["Desert", "Ocean", "Forest", "Mountain", "Tundra", "Space"])
        form_layout.addRow("Environment:", self.environment)

        # Add spacing
        main_layout.addSpacing(40)

        # Create buttons layout
        buttons_layout = QVBoxLayout()
        buttons_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addLayout(buttons_layout)

        # Generate button
        self.generate_button = SciFiButton.Normal("Generate")
        self.generate_button.setFixedSize(200, 40)
        buttons_layout.addWidget(self.generate_button)

        # Add spacing between buttons
        buttons_layout.addSpacing(20)

        # Back button
        self.back_button = SciFiButton.Normal("Back")
        self.back_button.setFixedSize(200, 40)
        buttons_layout.addWidget(self.back_button)

        # Connect back button to request navigation via mediator
        self.back_button.clicked.connect(self._on_back_clicked)

    def _on_back_clicked(self):
        if self.mediator:
            self.mediator.navigate_to(ScreenType.MAIN_MENU)