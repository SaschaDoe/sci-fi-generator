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

        self._generated_container = QWidget()
        self._generated_layout = QFormLayout(self._generated_container)
        self._generated_layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        self._generated_layout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self._generated_layout.setSpacing(8)

        self._generated_container.setStyleSheet("""
            font-size: 16px;
            color: #00FFFF;
            border: 2px solid #00FFFF;
            padding: 16px;
            border-radius: 12px;
            background-color: rgba(10, 20, 40, 0.75);
        """)
        self._generated_container.setVisible(False)

        main_layout.addWidget(self._generated_container)

        # Spacer to push buttons to bottom
        main_layout.addStretch(1)

        from ui.components.button.sci_fi_button import SciFiButton

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

    @Slot(object, object)
    def _handle_navigation(self, screen_type, data):
        if self.mediator:
            self.mediator.navigate_to(screen_type, data)

    @Slot(object)
    def _display_generated_civilization(self, civ):
        # Clear previous layout content
        while self._generated_layout.count():
            item = self._generated_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        def format_text(value):
            return value.name.replace('_', ' ').title()

        # Leader button
        leader_button = SciFiButton.Inline(civ.leader.name)
        leader_button.clicked.connect(lambda: self.view_model.request_leader_navigation(civ.leader))

        self._generated_layout.addRow(QLabel("<b>Name:</b>"), QLabel(civ.name))
        self._generated_layout.addRow(QLabel("<b>Leader:</b>"), leader_button)
        self._generated_layout.addRow(QLabel("<b>Origin:</b>"), QLabel(format_text(civ.origin_event)))
        self._generated_layout.addRow(QLabel("<b>Culture:</b>"), QLabel(format_text(civ.culture)))
        self._generated_layout.addRow(QLabel("<b>Social Structure:</b>"), QLabel(format_text(civ.social_structure)))
        self._generated_layout.addRow(QLabel("<b>Migration Pattern:</b>"), QLabel(format_text(civ.migration_pattern)))
        self._generated_layout.addRow(QLabel("<b>Dominant Profession:</b>"),
                                      QLabel(format_text(civ.dominant_profession)))


        self._generated_container.setVisible(True)

