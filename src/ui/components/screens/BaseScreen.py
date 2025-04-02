from abc import abstractmethod

from PySide6.QtWidgets import QWidget

from ui.navigation import ScreenType
from ui.navigation.mediator import INavigationMediator


class BaseScreen(QWidget):
    """
    Base class for all application screens.

    All screens in the application should inherit from this class
    to ensure they can be properly managed by the navigation system.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.mediator = None

    @property
    @abstractmethod
    def screen_type(self) -> ScreenType:
        """The type identifier for this screen."""
        pass

    def set_mediator(self, mediator: INavigationMediator) -> None:
        """Set the mediator for this screen to use for navigation."""
        self.mediator = mediator