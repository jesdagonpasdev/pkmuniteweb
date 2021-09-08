from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from fastapi_app.database.database import Base
from fastapi_app.database.models import ItemType

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    summary = Column(String)
    image = Column(String)
    type = Column(Enum(ItemType), nullable=False)

    attributes = relationship("Attribute", back_populates="item")
