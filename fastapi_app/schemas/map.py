from typing import List, Optional
from pydantic import BaseModel

class Map(BaseModel):
    id: int
    name: str
    image: Optional[str] = None
    players: int
    battle_time: Optional[int] = None
    battle_mode: str

    # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
    # (or any other arbitrary object with attributes). So, in will try to read data["id"] and also data.id
    class Config:
        orm_mode = True


class MapCreate(BaseModel):
    name: str
    image: Optional[str] = None
    players: int
    battle_time: Optional[int] = None
    battle_mode: str