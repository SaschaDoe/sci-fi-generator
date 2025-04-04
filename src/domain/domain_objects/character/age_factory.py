import random

class AgeFactory:
    @staticmethod
    def generate_age():
        weights = []
        for age in range(10, 101):
            # Gaussian-ish: peak around 30
            weight = max(0, 100 - abs(30 - age)**2)
            weights.append(weight)

        return random.choices(range(10, 101), weights=weights)[0]
