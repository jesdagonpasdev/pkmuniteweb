import enum

from typing import Optional
from pydantic import BaseModel, Field

class ItemType(str, enum.Enum):
    HELDS = "HELDS"
    BATTLE = "BATTLE"

class Item(BaseModel):
    id: int = Field(..., description="Item's identifier in the database.", example=1)
    name: str = Field(..., description="Item's name.", example="Leftovers")
    image: Optional[str] = Field(None, description="Image of the item.", example="https://www.pokemonunite.gg/res/img/item/leftovers.png")
    description: str = Field(..., description="Item's description.", example="When the Pokémon is not in combat, it recovers 1% of its max HP every second.")
    summary: str = Field(..., description="Item's short description.", example="Recovers 1% max HP every second out of combat.")
    type: ItemType = Field(..., description="Item's type.", example="HELDS")

    # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
    # (or any other arbitrary object with attributes). So, in will try to read data["id"] and also data.id
    class Config:
        orm_mode = True

class ItemCreate(BaseModel):
    name: str = Field(..., description="Item's name.", example="Eject Button")
    image: Optional[str] = Field(None, description="Image of the item.", example="https://www.pokemonunite.gg/res/img/battleitem/eject_button.png")
    description: str = Field(..., description="Item's description.", example="Quickly moves your Pokémon in the designated direction.")
    summary: str = Field(..., description="Item's short description.", example="Instantly teleport yourself somewhere nearby.")
    type: ItemType = Field(..., description="Item's type.", example="BATTLE")