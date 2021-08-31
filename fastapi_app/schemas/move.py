import enum

from typing import List, Optional
from pydantic import BaseModel, Field


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


class MoveBase(BaseModel):    
    pokemon_id: int = Field(..., description="Identifier of the Pokemon to which the move belongs to.", example=1)
    name: str = Field(..., description="Move's name.", example="Thunder")
    description: Optional[str] = Field(..., description="Move's details.", example="Throw a thunder in an area that stun the enemies.")
    type: MoveType  = Field(..., description="Move's type.", example="AREA")
    image: Optional[str] = Field(..., description="Move's image.", example="https://thunder.jpg")
    level: int = Field(..., description="Level to which the pokemon learn the move.", example=6)
    set: MoveSet = Field(..., description="Set to which the move belongs to.", example="FIRST_SET")
    cool_down: int = Field(..., description="Time, in second, to use the move again.", example=8)

class Move(MoveBase):
    id: int = Field(..., description="Move's identifier in the database.", example=1)

class MoveCreate(MoveBase):
    pass
