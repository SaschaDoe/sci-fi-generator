import pytest

from domain.tables.world.biomes import Biome
from domain.tables.world.geographic_features import GeographicFeature
from domain.tables.world.hydrological_features import HydrologicalFeature
from domain.tables.world.locational_terrains import LocationalTerrain
from domain.domain_objects.world.terrain import Terrain

@pytest.mark.fast
def test_valid_terrain_creation():
    terrain = Terrain(
        biome=Biome.FOREST,
        features=[GeographicFeature.HILLS, GeographicFeature.PLATEAUS],
        hydrology=[HydrologicalFeature.RIVERS],
        location=LocationalTerrain.HIGHLANDS
    )
    assert terrain.biome == Biome.FOREST
    assert GeographicFeature.HILLS in terrain.features
    assert HydrologicalFeature.RIVERS in terrain.hydrology
    assert terrain.location == LocationalTerrain.HIGHLANDS
@pytest.mark.fast
def test_invalid_biome_for_location():
    with pytest.raises(ValueError, match="Biome 'jungle' is not allowed in location 'highlands'"):
        Terrain(
            biome=Biome.JUNGLE,
            features=[GeographicFeature.HILLS],
            hydrology=[HydrologicalFeature.RIVERS],
            location=LocationalTerrain.HIGHLANDS
        )
@pytest.mark.fast
def test_describe_output():
    terrain = Terrain(
        biome=Biome.DESERT,
        features=[GeographicFeature.VALLEYS],
        hydrology=[HydrologicalFeature.OASES],
        location=LocationalTerrain.INLAND
    )
    description = terrain.describe()
    assert description == {
        "biome": "desert",
        "location": "inland",
        "features": ["valleys"],
        "hydrology": ["oases"]
    }
