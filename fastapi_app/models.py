from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from .database import Base

### MAP ###

class Map(Base):

    __tablename__ = "maps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    image = Column(String)
    players = Column(Integer)
    battle_time = Column(Integer)
    battle_mode = Column(String)

class BattleMode(str, Enum):
    STANDARD = "STANDARD"
    RANKED = "RANKED"
    QUICK = "QUICK"

###########

### POKEMON ###

class Pokemon(Base):

    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    image = Column(String)
    type = Column(String)  # PokemonType
    difficulty = Column(String)  # PokemonDifficulty
    video = Column(String)
    street = Column(String)  # MapStreet
    attack_type = Column(String)  # PokemonAttackType

class PokemonType(str, Enum):
    ATTACKER = "ATTACKER"
    SPEEDSTER = "SPEEDSTER"
    DEFENDER = "DEFENDER"
    ALLROUNDER = "ALL-ROUNDER"
    SUPPORTER = "SUPPORTER"

class PokemonDifficulty(str, Enum):
    NOVICE = "NOVICE"
    INTERMEDIATE = "INTERMEDIATE"
    EXPERT = "EXPERT"

class MapStreet(str, Enum):
    TOP = "TOP"
    MID = "MID"
    BOTTOM = "BOTTOM"

class PokemonAttackType(str, Enum):
    SPECIAL = "SPECIAL"
    PHYSICAL = "PHYSICAL"

###############

### STADISTICS ###

class Stadistic(Base):

    __tablename__ = "stadistics"
    

##################

### ITEM ###

class Item(Base):

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    summary = Column(String)
    image = Column(String)
    type = Column(String)

class Attribute(Base):

    __tablename__ = "attributes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    min_value = Column(Integer)
    max_value = Column(Integer)
    
    item_id = relationship("Item", back_populates="owner")

class ItemType(str, Enum):
    HELDS = "HELDS"
    BATTLE = "BATTLE"

###########