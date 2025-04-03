from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (
    QVBoxLayout, QLineEdit, QLabel, QWidget, QFormLayout
)
from ui.components.button.sci_fi_button import SciFiButton
from ui.components.screens.BaseScreen import BaseScreen
from ui.components.screens.civilisation_generation_viewmodel import CivilizationViewModel
from ui.navigation.ScreenType import ScreenType
from ui.navigation.mediator import INavigationMediator


class CivilizationScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        self.mediator = None
        self.view_model = CivilizationViewModel(self)

        self._name_input = None
        self._generate_button = None
        self._back_button = None
        self._generated_label = None

        self._setup_ui()
        self._connect_signals()
        self._apply_initial_state()

    @property
    def screen_type(self) -> ScreenType:
        return ScreenType.CIVILIZATION

    def set_mediator(self, mediator: INavigationMediator):
        self.mediator = mediator

    def _setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(80, 40, 80, 40)
        main_layout.setSpacing(24)

        # Title
        title_label = QLabel("🪐 Civilization Generator")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: #00FFFF;
            letter-spacing: 1px;
            text-shadow: 0 0 6px #00FFFF;
        """)
        main_layout.addWidget(title_label)

        # Result Display
        self._generated_label = QLabel(" ")
        self._generated_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._generated_label.setWordWrap(True)
        self._generated_label.setStyleSheet("""
            font-size: 16px;
            color: #00FFFF;
            border: 2px solid #00FFFF;
            padding: 16px;
            border-radius: 12px;
            background-color: rgba(10, 20, 40, 0.75);
            box-shadow: 0px 0px 12px #00FFFF;
        """)
        main_layout.addWidget(self._generated_label)
        self._generated_label.setVisible(False)

        # Spacer to push buttons to bottom
        main_layout.addStretch(1)

        # Generate button
        self._generate_button = SciFiButton.Normal("Generate Civilization")
        self._generate_button.setFixedSize(240, 44)
        main_layout.addWidget(self._generate_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Back Button under Generate
        self._back_button = SciFiButton.Normal("Back")
        self._back_button.setFixedSize(200, 36)
        main_layout.addWidget(self._back_button, alignment=Qt.AlignmentFlag.AlignCenter)

    def _connect_signals(self):
        self._generate_button.clicked.connect(self.view_model.request_generation)
        self._back_button.clicked.connect(lambda: self.view_model.request_back_navigation(ScreenType.MAIN_MENU))
        self.view_model.civilization_generated.connect(self._display_generated_civilization)
        self.view_model.navigation_requested.connect(self._handle_navigation)

    def _apply_initial_state(self):
        pass
    @Slot(object)
    def _handle_navigation(self, screen_type):
        if self.mediator:
            self.mediator.navigate_to(screen_type)

    @Slot(object)
    def _display_generated_civilization(self, civ):
        text = f"""
        <div style='font-size: 16px; color: #00FFFF;'>
            <table style='width: 100%; border-collapse: collapse;'>
                <tr><td style='padding: 6px; text-align: left;'><b>Name:</b></td><td style='text-align: right;'>{civ.name}</td></tr>
                <tr><td style='padding: 6px; text-align: left;'><b>Origin:</b></td><td style='text-align: right;'>{civ.origin_event.name.replace('_', ' ').title()}</td></tr>
                <tr><td style='padding: 6px; text-align: left;'><b>Culture:</b></td><td style='text-align: right;'>{civ.culture.name.replace('_', ' ').title()}</td></tr>
                <tr><td style='padding: 6px; text-align: left;'><b>Social Structure:</b></td><td style='text-align: right;'>{civ.social_structure.name.replace('_', ' ').title()}</td></tr>
                <tr><td style='padding: 6px; text-align: left;'><b>Migration Pattern:</b></td><td style='text-align: right;'>{civ.migration_pattern.name.replace('_', ' ').title()}</td></tr>
                <tr><td style='padding: 6px; text-align: left;'><b>Dominant Profession:</b></td><td style='text-align: right;'>{civ.dominant_profession.name.replace('_', ' ').title()}</td></tr>
            </table>
        </div>
        """
        self._generated_label.setText(text)
        self._generated_label.setVisible(True)

