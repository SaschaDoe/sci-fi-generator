from enum import Enum, auto


class ScreenType(Enum):
    """
    Defines the different screen types available in the application.

    This enum is used for navigation between different screens via the
    mediator pattern, allowing screens to request navigation without
    direct coupling to other screens.
    """

    MAIN_MENU = auto()
    """The main menu screen."""

    CIVILIZATION = auto()
    """The civilization generation screen"""

    LEADER = auto()
    """The leader (of a civilisation) screen"""