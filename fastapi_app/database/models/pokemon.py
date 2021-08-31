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

    stadistics = relationship("Stadistics", back_populates="pokemon")
    prices = relationship("PokemonPrice", back_populates="pokemon")
    skins = relationship("Skin", back_populates="pokemon")
    moves = relationship("Move", back_populates="pokemon")


class Stadistics(Base):
    __tablename__ = "stadistics"
    
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"), primary_key=True, index=True)
    offense = Column(Float, nullable=False, default=0)
    endurance = Column(Float, nullable=False, default=0)
    mobility = Column(Float, nullable=False, default=0)
    scoring = Column(Float, nullable=False, default=0)
    support = Column(Float, nullable=False, default=0)

    pokemon = relationship("Pokemon", back_populates="stadistics")


class PokemonPrice(Base):
    __tablename__ = "pokemon_prices"
    
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"), primary_key=True, index=True)
    aeos_coins = Column(Integer, nullable=False, default=0)
    aeos_gems = Column(Integer, nullable=False, default=0)

    pokemon = relationship("Pokemon", back_populates="prices")


class Skin(Base):
    __tablename__ = "skins"

    id = Column(Integer, primary_key=True, index=True)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"))
    image = Column(String)
    gems_cost = Column(Integer, nullable=False, default=0)

    pokemon = relationship("Pokemon", back_populates="skins")