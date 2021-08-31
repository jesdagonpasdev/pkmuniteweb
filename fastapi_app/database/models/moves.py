import enum

from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from fastapi_app.database.database import Base


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
    BASIC = 0
    FIRST_SET = 1
    SECOND_SET = 2
    UNITE_MOVE = 3
    PASIVE = 4


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