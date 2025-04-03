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
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        main_layout.setContentsMargins(80, 40, 80, 40)
        main_layout.setSpacing(24)

        title_label = QLabel("🪐 Civilization Generator")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: cyan;")
        main_layout.addWidget(title_label)

        # Form with name input only
        form_container = QWidget()
        form_layout = QFormLayout(form_container)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignHCenter)
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form_layout.setContentsMargins(20, 10, 20, 10)

        self._name_input = QLineEdit()
        self._name_input.setPlaceholderText("Enter a civilization name (or leave blank)")
        form_layout.addRow("Name:", self._name_input)

        main_layout.addWidget(form_container)

        # Generate button
        self._generate_button = SciFiButton.Normal("Generate Civilization")
        self._generate_button.setFixedSize(240, 44)
        main_layout.addWidget(self._generate_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Generated result display
        self._generated_label = QLabel("No civilization generated yet.")
        self._generated_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._generated_label.setWordWrap(True)
        self._generated_label.setStyleSheet("""
            font-size: 16px;
            color: #E0E0E0;
            border: 1px solid #444;
            padding: 16px;
            border-radius: 8px;
            background-color: rgba(20, 20, 30, 0.6);
        """)
        main_layout.addWidget(self._generated_label)

        # Back button
        self._back_button = SciFiButton.Normal("Back")
        self._back_button.setFixedSize(200, 36)
        main_layout.addWidget(self._back_button, alignment=Qt.AlignmentFlag.AlignCenter)

    def _connect_signals(self):
        self._generate_button.clicked.connect(self.view_model.request_generation)
        self._back_button.clicked.connect(lambda: self.view_model.request_back_navigation(ScreenType.MAIN_MENU))
        self._name_input.textChanged.connect(self.view_model.set_civilization_name)

        self.view_model.civilization_generated.connect(self._display_generated_civilization)
        self.view_model.navigation_requested.connect(self._handle_navigation)

    def _apply_initial_state(self):
        self.view_model.set_civilization_name(self._name_input.text())

    @Slot(object)
    def _handle_navigation(self, screen_type):
        if self.mediator:
            self.mediator.navigate_to(screen_type)

    @Slot(object)
    def _display_generated_civilization(self, civ):
        text = (
            f"<h3 style='color: cyan;'>{civ.name}</h3>"
            f"<p><b>Origin:</b> {civ.origin_event.name.replace('_', ' ').title()}</p>"
            f"<p><b>Culture:</b> {civ.culture.name.replace('_', ' ').title()}</p>"
            f"<p><b>Social Structure:</b> {civ.social_structure.name.replace('_', ' ').title()}</p>"
            f"<p><b>Migration Pattern:</b> {civ.migration_pattern.name.replace('_', ' ').title()}</p>"
            f"<p><b>Dominant Profession:</b> {civ.dominant_profession.name.replace('_', ' ').title()}</p>"
        )
        self._generated_label.setText(text)
