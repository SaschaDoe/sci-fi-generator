import sys

from PySide6.QtTest import QTest

from main import main
import pytest
from PySide6.QtWidgets import QApplication


@pytest.fixture
def app_fixture():
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    yield app

    app.quit()


def test_window_opens(app_fixture):
    # Call the main function
    window, _ = main()

    # Wait for the window to appear
    QTest.qWait(100)

    # Verify the window is visible
    assert window.isVisible() is True

    # Verify window has size
    assert window.width() > 0
    assert window.height() > 0

    # Clean up
    window.close()