from enum import Enum

class EarlyLifeEvent(Enum):
    ORPHANED = "Orphaned young"
    PRIVILEGED = "Born into nobility"
    FARM_CHILDHOOD = "Raised on a farm"
    SLUMS = "Grew up in the slums"

class AdulteryLifeEvent(Enum):
    LOST_LOVE = "Lost a great love"
    SECRET_AFFAIRS = "Had many secret affairs"
    MARRIED_YOUNG = "Married young"

class AdultLifeEvent(Enum):
    WARRIOR_PATH = "Fought in great wars"
    SCHOLAR_PATH = "Studied ancient wisdom"
    TRADER_PATH = "Became a successful trader"

class LeadershipEvent(Enum):
    REVOLUTION = "Led a revolution"
    FOUNDING = "Founded a colony"
    INHERITANCE = "Inherited the leadership"
    ELECTION = "Elected by the people"
