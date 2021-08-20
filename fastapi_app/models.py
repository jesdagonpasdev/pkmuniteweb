from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Map(Base):

    __tablename__ = "maps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    image = Column(String)
    players = Column(Integer)
    battle_time = Column(Integer)
    battle_modes = Column()