import enum

from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Float
from sqlalchemy.orm import relationship

from fastapi_app.database.database import Base


class MapStreet(str, enum.Enum):
    TOP = "TOP"
    MID = "MID"
    BOTTOM = "BOTTOM"
    ALL = "ALL"


class PokemonType(str, enum.Enum):
    ALL_ROUNDER = "ALL_ROUNDER"
    ATTACKER = "ATTACKER"
    DEFENDER = "DEFENDER"
    SPEEDSTER = "SPEEDSTER"
    SUPPORTER = "SUPPORTER"


class PokemonDifficulty(str, enum.Enum):
    NOVICE = "NOVICE"
    INTERMEDIATE = "INTERMEDIATE"
    EXPERT = "EXPERT"


class AttackType(str, enum.Enum):
    SPECIAL = "SPECIAL"
    PHYSICAL = "PHYSICAL"


class MoveType(str, enum.Enum):
    AREA = "AREA"
    BUFF = "BUFF"
    DASH = "DASH"
    DEBUFF = "DEBUFF"
    HINDRANCE = "HINDRANCE"
    MELEE = "MELEE"
    RANGED = "RANGED"
    RECOVERY = "RECOVERY"
    SURE_HIT = "SURE_HIT"


class MoveSet(str, enum.Enum):
    BASIC = "BASIC"
    FIRST_SET = "FIRST_SET"
    SECOND_SET = "SECOND_SET"
    UNITE_MOVE = "UNITE_MOVE"
    PASIVE = "PASIVE"

class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(Enum(PokemonType), nullable=False)
    difficulty = Column(Enum(PokemonDifficulty), nullable=False)
    street = Column(Enum(MapStreet), nullable=False)
    attack_type = Column(Enum(AttackType), nullable=False)
    image = Column(String)
    video = Column(String)

    stadistics = relationship("Stadistics", back_populates="pokemon", uselist=False, cascade="all, delete")
    prices = relationship("PokemonPrice", back_populates="pokemon", uselist=False, cascade="all, delete")
    skins = relationship("Skin", back_populates="pokemon", cascade="all, delete")
    moves = relationship("Move", back_populates="pokemon", cascade="all, delete")


class Stadistics(Base):
    __tablename__ = "stadistics"
    
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"), primary_key=True, index=True)
    offense = Column(Float, nullable=False)
    endurance = Column(Float, nullable=False)
    mobility = Column(Float, nullable=False)
    scoring = Column(Float, nullable=False)
    support = Column(Float, nullable=False)

    pokemon = relationship("Pokemon", back_populates="stadistics", uselist=False)


class PokemonPrice(Base):
    __tablename__ = "pokemon_prices"
    
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"), primary_key=True, index=True)
    aeos_coins = Column(Integer, nullable=False)
    aeos_gems = Column(Integer, nullable=False)

    pokemon = relationship("Pokemon", back_populates="prices", uselist=False)


class Skin(Base):
    __tablename__ = "skins"

    id = Column(Integer, primary_key=True, index=True)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"))
    image = Column(String)
    gems_cost = Column(Integer, nullable=False)

    pokemon = relationship("Pokemon", back_populates="skins")


class Move(Base):
    __tablename__ = "moves"

    id = Column(Integer, primary_key=True, index=True)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"))
    name = Column(String, nullable=False)
    description = Column(String)
    type = Column(Enum(MoveType), nullable=False)
    image = Column(String)
    level = Column(Integer, nullable=False)
    set = Column(Enum(MoveSet), nullable=False)
    cool_down = Column(Integer, nullable=False)

    pokemon = relationship("Pokemon", back_populates="moves")