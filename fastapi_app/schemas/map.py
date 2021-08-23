import enum

from typing import List, Optional
from pydantic import BaseModel, Field


class BattleMode(str, enum.Enum):
    STANDARD = "STANDARD"
    RANKED = "RANKED"
    QUICK = "QUICK"

class Map(BaseModel):
    id: int = Field(..., description="Map's identifier in the database.", example=1)
    name: str = Field(..., description="Map's name.", example="Remoat Stadium")
    image: Optional[str] = Field(None, description="Image of the map.", example="http://rStadium.com/rStadium.jpeg")
    players: int = Field(..., description="Number of player (per team) in the map.", example=5)
    battle_time: Optional[int] = Field(None, description="Time (in minutes) of each battle in the map.", example=10)
    battle_mode: BattleMode  = Field(..., description="Battle mode of the map.", example="STANDARD")

    # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
    # (or any other arbitrary object with attributes). So, in will try to read data["id"] and also data.id
    class Config:
        orm_mode = True


class MapCreate(BaseModel):
    name: str = Field(..., description="New Map's name.", example="New Stadium")
    image: Optional[str] = Field(None, description="New Map's image.", example="http://newStadium.com/newStadium.jpeg")
    players: int = Field(..., description="Number of player (per team) in the new map.", example=3)
    battle_time: Optional[int] = Field(None, description="Time (in minutes) of each battle in the new map.", example=3)
    battle_mode: BattleMode  = Field(..., description="Battle mode of the new map.", example="QUICK")
