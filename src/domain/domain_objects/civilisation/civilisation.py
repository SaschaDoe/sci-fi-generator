from dataclasses import dataclass

from domain.domain_objects.character.leader.leader import Leader
from domain.tables.civilisation.civilization_origin_event import CivilizationOriginEvent
from domain.tables.civilisation.culture import CultureType
from domain.tables.civilisation.migration_pattern import MigrationPattern
from domain.tables.civilisation.modern_civilisation_professions import ModernCivilisationProfession
from domain.tables.civilisation.social_structure import SocialStructure


@dataclass
class Civilization:
    name: str
    origin_event: CivilizationOriginEvent
    culture: CultureType
    social_structure: SocialStructure
    migration_pattern: MigrationPattern
    dominant_profession: ModernCivilisationProfession
    leader: Leader