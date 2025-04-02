from PySide6.QtCore import QObject, Signal, Property

class CivilizationViewModel(QObject):
    """
    Manages the state and logic for the Civilization Generation Screen.
    """
    # --- Signals indicating state changes for the View ---
    content_visibility_changed = Signal(bool)
    generate_button_text_changed = Signal(str)
    # Signal to tell the view to navigate
    navigation_requested = Signal(object) # object can be ScreenType enum

    def __init__(self, parent=None):
        super().__init__(parent)

        # --- Internal State ---
        self._is_content_visible = False
        self._generate_button_text = "Generate"
        # Add properties for inputs if needed for complex logic/validation
        self._civilization_name = ""
        self._tech_level = ""
        # ... other inputs

    # --- Properties (Optional but good practice for QML/complex binding) ---
    # Read-only properties exposing state controlled by this ViewModel
    @Property(bool, notify=content_visibility_changed)
    def is_content_visible(self):
        return self._is_content_visible

    @Property(str, notify=generate_button_text_changed)
    def generate_button_text(self):
        return self._generate_button_text

    # --- Public Methods / Slots (Actions triggered by the View) ---

    def request_generation(self):
        """Handles the logic when the generate/generate again button is clicked."""
        print("ViewModel: Generation requested.") # Debug

        # First click logic
        if not self._is_content_visible:
            self._is_content_visible = True
            self.content_visibility_changed.emit(True) # Notify View

            self._generate_button_text = "Generate Again"
            self.generate_button_text_changed.emit(self._generate_button_text) # Notify View

        # --- Actual Generation Logic Here ---
        # This part runs every time the button is clicked.
        # You would likely gather input values (potentially passed from View
        # or stored via setters) and call a generation service/function.
        print(f"ViewModel: Triggering actual generation with inputs:")
        print(f"  Name: {self._civilization_name}")
        print(f"  Tech: {self._tech_level}")
        # result = generation_service.generate(name=self._civilization_name, ...)
        # Maybe emit another signal with the result?
        # self.generation_completed.emit(result)

    def request_back_navigation(self, screen_type):
        """Signals that navigation back to the specified screen is requested."""
        print("ViewModel: Back navigation requested.") # Debug
        # Optional: Reset internal state before navigating away
        self.reset_state()
        self.navigation_requested.emit(screen_type)

    def reset_state(self):
        """Resets the ViewModel to its initial state."""
        if self._is_content_visible: # Only reset if changes were made
             print("ViewModel: Resetting state.") # Debug
             self._is_content_visible = False
             self.content_visibility_changed.emit(False)

             self._generate_button_text = "Generate"
             self.generate_button_text_changed.emit(self._generate_button_text)

             # Reset input trackers if necessary
             self._civilization_name = ""
             self._tech_level = ""
             # ...

    # --- Setters for inputs (called by the View) ---
    # Use these if the ViewModel needs the input data for its logic

    def set_civilization_name(self, name: str):
        self._civilization_name = name
        # print(f"ViewModel: Name set to {name}") # Debug

    def set_tech_level(self, level: str):
        self._tech_level = level
        # print(f"ViewModel: Tech Level set to {level}") # Debug

    def set_social_structure(self, structure: str):
        # Store if needed
        pass

    def set_environment(self, environment: str):
        # Store if needed
        pass