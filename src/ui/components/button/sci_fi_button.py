from PySide6.QtWidgets import QPushButton

from ui.components.button.sci_fi_button_styles import SCI_FI_BUTTON_EXIT, SCI_FI_BUTTON_BASE,  \
    SCI_FI_BUTTON_INLINE


class SciFiButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

    @classmethod
    def Normal(cls, text="NEW", parent=None):
        button = cls(text, parent)
        button.setStyleSheet(SCI_FI_BUTTON_BASE)
        return button

    @classmethod
    def Inline(cls, text="Click", parent=None):
        button = cls(text, parent)
        button.setStyleSheet(SCI_FI_BUTTON_INLINE)
        return button

    @classmethod
    def Exit(cls, text="EXIT", parent=None):
        button = cls(text, parent)
        button.setStyleSheet(SCI_FI_BUTTON_EXIT)
        return button
