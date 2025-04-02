# tests/ui/screens/test_civilization_view_model.py

import pytest
from PySide6.QtCore import QObject, Signal

# --- Adjust this import path to match YOUR project structure ---
try:
    from ui.components.screens.civilisation_generation_viewmodel import CivilizationViewModel
except ImportError:
    pytest.fail("Could not import CivilizationViewModel. Check import path.", pytrace=False)

# --- Adjust this import path for ScreenType if needed ---
try:
    from ui.navigation.ScreenType import ScreenType
except ImportError:
    from enum import Enum
    class ScreenType(Enum):
        MAIN_MENU = 1
        CIVILIZATION = 2
    ScreenType = None # Test requiring this will be skipped


# --- Test Class ---

class TestCivilizationViewModel:
    # Short wait time for signal processing
    PROCESS_EVENTS_TIMEOUT = 50 # milliseconds

    @pytest.fixture
    def view_model(self, qtbot) -> CivilizationViewModel:
        """Fixture to create a fresh ViewModel instance for each test."""
        vm = CivilizationViewModel()
        return vm

    def test_initial_state(self, view_model: CivilizationViewModel):
        """Verify the ViewModel's state upon initialization."""
        assert not view_model.is_content_visible
        assert view_model.generate_button_text == "Generate"

    def test_first_generation_request(self, view_model: CivilizationViewModel, qtbot):
        """Test the state changes and signal emissions on the first generation request."""
        received_args = {} # Dictionary to store received args

        # Define simple slots to capture arguments
        def on_vis_changed(visible):
            received_args['visibility'] = [visible]

        def on_text_changed(text):
            received_args['text'] = [text]

        # Connect slots BEFORE the action
        view_model.content_visibility_changed.connect(on_vis_changed)
        view_model.generate_button_text_changed.connect(on_text_changed)

        # --- Action ---
        view_model.request_generation()

        # Give time for signals to be processed
        qtbot.wait(self.PROCESS_EVENTS_TIMEOUT)

        # --- Assert State Changes ---
        assert view_model.is_content_visible, "Content should become visible"
        assert view_model.generate_button_text == "Generate Again", "Button text should change"

        # --- Assert Captured Signal Arguments ---
        assert received_args.get('visibility') == [True], f"Visibility signal expected [True], got {received_args.get('visibility')}"
        assert received_args.get('text') == ["Generate Again"], f"Text signal expected ['Generate Again'], got {received_args.get('text')}"

        # Optional: Disconnect signals (good practice)
        try:
            view_model.content_visibility_changed.disconnect(on_vis_changed)
            view_model.generate_button_text_changed.disconnect(on_text_changed)
        except RuntimeError: pass # Ignore if already disconnected or error occurred


    @pytest.mark.skipif(ScreenType is None, reason="ScreenType enum not available")
    def test_back_navigation_request(self, view_model: CivilizationViewModel, qtbot):
        """Test the back navigation request signal and implicit state reset."""
        # --- Setup: Trigger first generation ---
        view_model.request_generation()
        qtbot.wait(self.PROCESS_EVENTS_TIMEOUT)

        target_screen = ScreenType.MAIN_MENU
        received_args = {}
        def on_nav_requested(screen): received_args['nav'] = [screen]
        def on_vis_changed(visible): received_args['visibility'] = [visible]
        def on_text_changed(text): received_args['text'] = [text]

        view_model.navigation_requested.connect(on_nav_requested)
        view_model.content_visibility_changed.connect(on_vis_changed)
        view_model.generate_button_text_changed.connect(on_text_changed)

        # --- Action: Request navigation ---
        view_model.request_back_navigation(target_screen)
        qtbot.wait(self.PROCESS_EVENTS_TIMEOUT) # Wait for signals

        # --- Assert Implicit State Reset ---
        assert not view_model.is_content_visible, "State should reset on back navigation"
        assert view_model.generate_button_text == "Generate", "State should reset on back navigation"

        # --- Assert Captured Signal Arguments ---
        assert received_args.get('nav') == [target_screen], f"Navigation signal expected [{target_screen}], got {received_args.get('nav')}"
        assert received_args.get('visibility') == [False], f"Visibility reset signal expected [False], got {received_args.get('visibility')}"
        assert received_args.get('text') == ["Generate"], f"Text reset signal expected ['Generate'], got {received_args.get('text')}"

        try:
            view_model.navigation_requested.disconnect(on_nav_requested)
            view_model.content_visibility_changed.disconnect(on_vis_changed)
            view_model.generate_button_text_changed.disconnect(on_text_changed)
        except RuntimeError: pass