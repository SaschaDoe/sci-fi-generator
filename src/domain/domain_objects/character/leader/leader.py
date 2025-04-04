from dataclasses import dataclass
from typing import List

from domain.domain_objects.character.attributes import Attributes


@dataclass
class Leader:
    name: str
    profession: str
    convictions: List[str]
    social_class: str
    age: int
    gender: str
    life_events: List[str]
    attributes: Attributes


