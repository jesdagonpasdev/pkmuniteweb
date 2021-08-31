import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from fastapi_app.database.database import Base

class ItemType(str, enum.Enum):
    HELDS = "HELDS"
    BATTLE = "BATTLE"


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    summary = Column(String)
    image = Column(String)
    type = Column(Enum(ItemType), nullable=False)

    attributes = relationship("Attribute", back_populates="item")


class Attribute(Base):
    __tablename__ = "attributes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    min_value = Column(Integer, default=0)
    max_value = Column(Integer, default=0)
    item_id = Column(Integer, ForeignKey("items.id"))

    item = relationship("Item", back_populates="attributes")