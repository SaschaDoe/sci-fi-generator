import sys
import pytest
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from main import main
from ui.navigation.ScreenType import ScreenType


@pytest.fixture
def app_fixture():
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    yield app

    app.quit()


@pytest.mark.ui
def test_exit_button_closes_window(app_fixture):
    # Call the main function
    window, _ = main()

    # Wait for the window to appear
    QTest.qWait(100)

    # Verify the window is visible initially
    assert window.isVisible() is True

    # Create a flag to track window closed state
    window_closed = False

    # Connect to the destroyed signal to verify window closure
    def on_window_destroyed():
        nonlocal window_closed
        window_closed = True

    window.destroyed.connect(on_window_destroyed)

    # Find and click the exit button
    main_menu_screen = window.mediator.screens[ScreenType.MAIN_MENU]

    # Now find the exit button within the main menu screen
    exit_button = main_menu_screen.exitButton
    assert exit_button is not None, "Exit button not found"

    # Click the button
    QTest.mouseClick(exit_button, Qt.MouseButton.LeftButton)

    # Wait for events to process
    QTest.qWait(100)

    # Directly check if the window is visible after clicking the button
    # window.close() should make isVisible() return False
    assert window.isVisible() is False, "Window is still visible after clicking exit button"