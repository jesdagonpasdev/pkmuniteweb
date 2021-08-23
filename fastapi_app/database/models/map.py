import enum
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
    battle_mode = Column(Enum(BattleMode), nullable=False)
