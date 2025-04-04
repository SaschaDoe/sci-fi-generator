import random

from domain.domain_objects.character.leader.leader_factory import LeaderFactory
from domain.domain_objects.civilisation.civilisation import Civilization
from domain.tables.civilisation.civilization_origin_event import CivilizationOriginEvent
from domain.tables.civilisation.culture import CultureType
from domain.tables.civilisation.migration_pattern import MigrationPattern
from domain.tables.civilisation.modern_civilisation_professions import ModernCivilisationProfession
from domain.tables.civilisation.social_structure import SocialStructure

class CivilizationFactory:
    def __init__(self, rng: random.Random):
        self.leader_factory = LeaderFactory(rng)
        self.rng = rng

    def create_random_civilization(self, name: str) -> Civilization:
        return Civilization(
            name=name,
            origin_event=self.rng.choice(list(CivilizationOriginEvent)),
            culture=self.rng.choice(list(CultureType)),
            social_structure=self.rng.choice(list(SocialStructure)),
            migration_pattern=self.rng.choice(list(MigrationPattern)),
            dominant_profession=self.rng.choice(list(ModernCivilisationProfession)),
            leader=self.leader_factory.create_leader(name),
        )