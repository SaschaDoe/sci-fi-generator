from PySide6.QtCore import Qt, Slot # Import Slot
from PySide6.QtWidgets import (
    QVBoxLayout, QComboBox, QLineEdit, QFormLayout, QLabel, QWidget,
    QSpacerItem, QSizePolicy
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

        # --- Create the ViewModel instance ---
        self.view_model = CivilizationViewModel(self) # Pass parent if needed for lifecycle

        # --- UI Element References ---
        # We still need references to manipulate them based on ViewModel signals
        self._title_label = None
        self._form_widget = None
        self._name_input = None
        self._tech_level_combo = None
        self._social_structure_combo = None
        self._environment_combo = None
        self._generate_button = None
        self._back_button = None
        # -----------------------------

        self._setup_ui()
        self._connect_signals()
        self._apply_initial_state() # Apply state after UI setup and connections

    @property
    def screen_type(self) -> ScreenType:
        return ScreenType.CIVILIZATION

    def set_mediator(self, mediator: INavigationMediator):
        self.mediator = mediator

    # --- UI Setup (Less Logic Here) ---
    def _setup_ui(self):
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        # Title (Created, but visibility controlled by VM)
        self._title_label = QLabel("Civilization Generator")
        self._title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self._title_label)

        main_layout.addSpacing(20)

        # Form Widget (Created, but visibility controlled by VM)
        self._form_widget = QWidget()
        form_layout = QFormLayout(self._form_widget)
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)

        # Inputs (Store references)
        self._name_input = QLineEdit()
        form_layout.addRow("Civilization Name:", self._name_input)

        self._tech_level_combo = QComboBox()
        self._tech_level_combo.addItems(["Primitive", "Industrial", "Modern", "Advanced", "Futuristic", "Post-Singularity"])
        form_layout.addRow("Technology Level:", self._tech_level_combo)

        self._social_structure_combo = QComboBox()
        self._social_structure_combo.addItems(["Tribal", "Feudal", "Democracy", "Republic", "Technocracy", "Hive Mind"])
        form_layout.addRow("Social Structure:", self._social_structure_combo)

        self._environment_combo = QComboBox()
        self._environment_combo.addItems(["Desert", "Ocean", "Forest", "Mountain", "Tundra", "Space"])
        form_layout.addRow("Environment:", self._environment_combo)

        main_layout.addWidget(self._form_widget)

        main_layout.addStretch(1)

        # Buttons Container
        buttons_container = QWidget()
        buttons_layout = QVBoxLayout(buttons_container)
        buttons_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Buttons (Store references, text/visibility controlled by VM)
        self._generate_button = SciFiButton.Normal("Generate") # Initial text set by VM later
        self._generate_button.setFixedSize(200, 40)
        buttons_layout.addWidget(self._generate_button)

        buttons_layout.addSpacing(20)

        self._back_button = SciFiButton.Normal("Back")
        self._back_button.setFixedSize(200, 40)
        buttons_layout.addWidget(self._back_button)

        main_layout.addWidget(buttons_container)
        main_layout.addStretch(1)

    # --- Connect UI Interactions and VM Signals ---
    def _connect_signals(self):
        # --- Connect View -> ViewModel Actions ---
        self._generate_button.clicked.connect(self.view_model.request_generation)
        self._back_button.clicked.connect(
            lambda: self.view_model.request_back_navigation(ScreenType.MAIN_MENU)
        )

        # Connect input changes to ViewModel setters
        self._name_input.textChanged.connect(self.view_model.set_civilization_name)
        self._tech_level_combo.currentTextChanged.connect(self.view_model.set_tech_level)
        self._social_structure_combo.currentTextChanged.connect(self.view_model.set_social_structure)
        self._environment_combo.currentTextChanged.connect(self.view_model.set_environment)


        # --- Connect ViewModel Signals -> View Update Slots ---
        self.view_model.content_visibility_changed.connect(self._update_content_visibility)
        self.view_model.generate_button_text_changed.connect(self._generate_button.setText)
        self.view_model.navigation_requested.connect(self._handle_navigation)

    # --- Apply Initial State from ViewModel ---
    def _apply_initial_state(self):
        """ Sets the initial UI state based on the ViewModel's current state. """
        self._update_content_visibility(self.view_model.is_content_visible)
        self._generate_button.setText(self.view_model.generate_button_text)
        # Set initial input values in VM if needed (or read from view if that's the flow)
        self.view_model.set_civilization_name(self._name_input.text())
        self.view_model.set_tech_level(self._tech_level_combo.currentText())
        # ... etc ...


    # --- Slots to Update UI based on ViewModel ---

    @Slot(bool)
    def _update_content_visibility(self, visible):
        """Updates the visibility of content elements."""
        print(f"View: Updating content visibility to {visible}") # Debug
        self._title_label.setVisible(visible)
        self._form_widget.setVisible(visible)
        self._back_button.setVisible(visible)

    @Slot(object) # Accepts the ScreenType enum
    def _handle_navigation(self, screen_type):
        """Handles navigation requests from the ViewModel."""
        if self.mediator:
            print(f"View: Handling navigation request to {screen_type}") # Debug
            self.mediator.navigate_to(screen_type)
        else:
             print("View Warning: Mediator not set, cannot navigate.")

    # Optional: Override showEvent to reset VM state if desired behaviour
    def showEvent(self, event):
        # Option 1: Reset every time screen is shown
        # self.view_model.reset_state()

        # Option 2: Do nothing special, state persists until explicitly reset (e.g., on back)
        super().showEvent(event) # Call base class