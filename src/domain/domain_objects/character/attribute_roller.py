import random

class AttributeRoller:
    @staticmethod
    def roll_attribute():
        return sum(random.randint(1, 6) for _ in range(3))
