from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

from ui.components.button.sci_fi_button_styles import SCI_FI_BUTTON_EXIT, SCI_FI_BUTTON_BASE


class SciFiButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

    @classmethod
    def New(cls, text="NEW", parent=None):
        button = cls(text, parent)
        button.setStyleSheet(SCI_FI_BUTTON_BASE)
        return button

    @classmethod
    def Exit(cls, text="EXIT", parent=None):
        button = cls(text, parent)
        button.setStyleSheet(SCI_FI_BUTTON_EXIT)
        return button
