from ui.components.screens.civilisation_generation_screen import CivilizationScreen
from ui.components.screens.leader_screen import LeaderScreen
from ui.components.screens.main_menu_screen import MainMenuScreen


def _setup_screens(self):
    """Create all screen widgets and register them with the mediator"""
    self._setup_screen(MainMenuScreen())
    self._setup_screen(CivilizationScreen())
    self._setup_screen(LeaderScreen())