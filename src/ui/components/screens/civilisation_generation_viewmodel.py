from PySide6.QtCore import QObject, Signal, Property

import random

from domain.domain_objects.civilisation.civilisation import Civilization
from domain.domain_objects.civilisation.civilisation_factory import CivilizationFactory


class CivilizationViewModel(QObject):
    """
    Manages the state and logic for the Civilization Generation Screen.
    """
    content_visibility_changed = Signal(bool)
    generate_button_text_changed = Signal(str)
    navigation_requested = Signal(object)
    civilization_generated = Signal(Civilization)

    def __init__(self, parent=None):
        super().__init__(parent)

        self._is_content_visible = False
        self._generate_button_text = "Generate"

        self._civilization_name = ""
        self._tech_level = ""
        self._social_structure = ""
        self._environment = ""

        self._factory = CivilizationFactory(random.Random())

    @Property(bool, notify=content_visibility_changed)
    def is_content_visible(self):
        return self._is_content_visible

    @Property(str, notify=generate_button_text_changed)
    def generate_button_text(self):
        return self._generate_button_text

    def request_generation(self):
        print("ViewModel: Generation requested.")

        if not self._is_content_visible:
            self._is_content_visible = True
            self.content_visibility_changed.emit(True)
            self._generate_button_text = "Generate Again"
            self.generate_button_text_changed.emit(self._generate_button_text)

        print(f"Generating with inputs: Name={self._civilization_name}, Tech={self._tech_level}, "
              f"Structure={self._social_structure}, Env={self._environment}")

        civilization = self._factory.create_random_civilization(self._civilization_name)
        self.civilization_generated.emit(civilization)

    def request_back_navigation(self, screen_type):
        print("ViewModel: Back navigation requested.")
        self.reset_state()
        self.navigation_requested.emit(screen_type)

    def reset_state(self):
        if self._is_content_visible:
            print("ViewModel: Resetting state.")
            self._is_content_visible = False
            self.content_visibility_changed.emit(False)

            self._generate_button_text = "Generate"
            self.generate_button_text_changed.emit(self._generate_button_text)

            self._civilization_name = ""
            self._tech_level = ""
            self._social_structure = ""
            self._environment = ""

    def set_civilization_name(self, name: str):
        self._civilization_name = name

    def set_tech_level(self, level: str):
        self._tech_level = level

    def set_social_structure(self, structure: str):
        self._social_structure = structure

    def set_environment(self, environment: str):
        self._environment = environment
