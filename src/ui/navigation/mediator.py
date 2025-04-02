from abc import ABC, abstractmethod

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget
from ui.navigation.ScreenType import ScreenType

class INavigationMediator:
    """Interface for navigation mediator"""

    def navigate_to(self, screen_type):
        """
        Navigate to the specified screen

        This method must be implemented by concrete mediators.
        """
        raise NotImplementedError("Subclasses must implement navigate_to")


class NavigationMediator(QObject, INavigationMediator):
    def __init__(self, main_window, close_callback=None):
        super().__init__()
        self.main_window = main_window
        self._close_callback = close_callback
        self.screens = {}

    def exit_application(self):
        """Exit the application"""
        self._close_callback()

    def register_screen(self, screen_type: ScreenType, screen_widget: QWidget):
        """Register a screen (as a widget) with the mediator"""
        self.screens[screen_type] = screen_widget

    def navigate_to(self, screen: ScreenType):
        """Navigate to the specified screen"""
        if screen in self.screens:
            self.main_window.stacked_widget.setCurrentWidget(self.screens[screen])
        else:
            print(f"Screen {screen} not registered with mediator")
