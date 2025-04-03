from typing import List

from domain.tables.world.biomes import Biome
from domain.tables.world.geographic_features import GeographicFeature
from domain.tables.world.hydrological_features import HydrologicalFeature
from domain.tables.world.locational_terrains import LOCATIONAL_COMPATIBILITY, LocationalTerrain


class Terrain:
    def __init__(
        self,
        biome: Biome,
        features: List[GeographicFeature],
        hydrology: List[HydrologicalFeature],
        location: LocationalTerrain
    ):
        self.biome = biome
        self.features = features
        self.hydrology = hydrology
        self.location = location

        self.validate()

    def validate(self):
        # Ensure biome is compatible with location
        allowed_biomes = LOCATIONAL_COMPATIBILITY.get(self.location, set())
        if self.biome not in allowed_biomes:
            raise ValueError(f"Biome '{self.biome.value}' is not allowed in location '{self.location.value}'")

    def describe(self):
        return {
            "biome": self.biome.value,
            "location": self.location.value,
            "features": [f.value for f in self.features],
            "hydrology": [h.value for h in self.hydrology],
        }