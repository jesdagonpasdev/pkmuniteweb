from typing import List, Optional
from pydantic import BaseModel

class Map(BaseModel):
    id: int
    name: str
    image: str
    players: int
    battle_time: int
    battle_mode: str

    class Config:
        orm_mode = True