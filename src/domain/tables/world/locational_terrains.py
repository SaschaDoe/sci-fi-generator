from enum import StrEnum, auto

from domain.tables.world.biomes import Biome


class LocationalTerrain(StrEnum):
    ISLAND = auto()
    COASTLINE = auto()
    PENINSULA = auto()
    ARCHIPELAGO = auto()
    INLAND = auto()
    HIGHLANDS = auto()
    LOWLANDS = auto()

# === Locational Compatibility Map ===

LOCATIONAL_COMPATIBILITY = {
    LocationalTerrain.ISLAND:        {Biome.JUNGLE, Biome.FOREST, Biome.DESERT, Biome.GRASSLAND},
    LocationalTerrain.COASTLINE:    set(Biome),
    LocationalTerrain.PENINSULA:    set(Biome),
    LocationalTerrain.ARCHIPELAGO:  {Biome.JUNGLE, Biome.FOREST, Biome.DESERT},
    LocationalTerrain.INLAND:       set(Biome),
    LocationalTerrain.HIGHLANDS:    {Biome.TUNDRA, Biome.FOREST, Biome.GRASSLAND, Biome.STEPPE},
    LocationalTerrain.LOWLANDS:     set(Biome),
}