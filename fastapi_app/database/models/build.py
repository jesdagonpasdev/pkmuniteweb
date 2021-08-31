from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from fastapi_app.database.database import Base
from fastapi_app.database.models import MapStreet


class Build(Base):
    __tablename__ = "builds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"), nullable=False)
    held_object_one = Column(Integer, ForeignKey("items.id"), nullable=False)
    held_object_two = Column(Integer, ForeignKey("items.id"), nullable=False)
    held_object_three = Column(Integer, ForeignKey("items.id"), nullable=False)
    battle_object = Column(Integer, ForeignKey("items.id"), nullable=False)
    first_movement = Column(Integer, ForeignKey("moves.id"), nullable=False)
    movement_one = Column(Integer, ForeignKey("moves.id"), nullable=False)
    movement_two = Column(Integer, ForeignKey("moves.id"), nullable=False)
    tips = Column(String)
    street = Column(Enum(MapStreet), nullable=False)

    build_partners = relationship("BuildPartner", back_populates="build")


class BuildPartner(Base):
    __tablename__ = "build_partners"

    build_id = Column(Integer, ForeignKey("builds.id"), primary_key=True, index=True)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"), primary_key=True, index=True)
    description = Column(String)

    build = relationship("Build", back_populates="build_partners")
