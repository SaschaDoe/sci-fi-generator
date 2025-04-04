import random

from domain.domain_objects.character.age_factory import AgeFactory
from domain.domain_objects.character.attribute_roller import AttributeRoller
from domain.domain_objects.character.leader.leader import Leader
from domain.domain_objects.character.attributes import Attributes
from domain.domain_objects.character.leader.live_events import LeadershipEvent, AdultLifeEvent, AdulteryLifeEvent, \
    EarlyLifeEvent
from domain.tables.character.convictions import Convictions
from domain.tables.character.gender import Gender
from domain.tables.civilisation.social_class import SocialClass


class LeaderFactory:
    def __init__(self, rng: random.Random):
        self.rng = rng

    def create_leader(self, civilization_name: str) -> Leader:
        name = "Mysterious Figure"
        profession = f"Leader of {civilization_name}" if civilization_name else "Civilization Leader"
        gender = self.rng.choice(list(Gender)).value
        social_class = self.rng.choice(list(SocialClass)).value
        convictions = [self.rng.choice(list(Convictions)).value]
        age = AgeFactory.generate_age()

        # Life events
        life_events = [self.rng.choice(list(EarlyLifeEvent)).value]
        if age >= 20:
            life_events.append(self.rng.choice(list(AdulteryLifeEvent)).value)
            life_events.append(self.rng.choice(list(AdultLifeEvent)).value)
        life_events.append(self.rng.choice(list(LeadershipEvent)).value)

        # Attributes
        attributes = Attributes(
            willpower=AttributeRoller.roll_attribute(),
            charisma=AttributeRoller.roll_attribute(),
            knowledge=AttributeRoller.roll_attribute(),
            intuition=AttributeRoller.roll_attribute(),
            dexterity=AttributeRoller.roll_attribute(),
            manual_dexterity=AttributeRoller.roll_attribute(),
            constitution=AttributeRoller.roll_attribute(),
            strength=AttributeRoller.roll_attribute(),
        )

        return Leader(
            name=name,
            profession=profession,
            convictions=convictions,
            social_class=social_class,
            age=age,
            gender=gender,
            life_events=life_events,
            attributes=attributes
        )
