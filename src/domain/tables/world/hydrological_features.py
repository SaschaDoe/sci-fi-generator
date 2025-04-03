from enum import StrEnum, auto


class HydrologicalFeature(StrEnum):
    RIVERS = auto()
    LAKES = auto()
    MARSHES = auto()
    SPRINGS = auto()
    OASES = auto()
    WATERFALLS = auto()