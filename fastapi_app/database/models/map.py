""" import enum
from sqlalchemy import Column, Integer, String, Enum

from fastapi_app.database.database import Base

class BattleMode(enum.Enum):
    STANDARD = "STANDARD"
    RANKED = "RANKED"
    QUICK = "QUICK"

class Map(Base):
    __tablename__ = "maps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    image = Column(String)
    players = Column(Integer, nullable=False)
    battle_time = Column(Integer)
    battle_mode = Column(Enum(BattleMode), nullable=False) """

import enum

from typing import Optional

from sqlmodel import Field, SQLModel


class BattleMode(str, enum.Enum):
    STANDARD = "STANDARD"
    RANKED = "RANKED"
    QUICK = "QUICK"


class Map(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    image: Optional[str]
    players: int
    battle_time: Optional[int] = None
    battle_mode: BattleMode
