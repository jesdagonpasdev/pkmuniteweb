import enum

from typing import List, Optional
from pydantic import BaseModel, Field

from fastapi_app.schemas.move import Move


class MapStreet(str, enum.Enum):
    TOP = "TOP"
    MID = "MID"
    BOTTOM = "BOTTOM"
    ALL = "ALL"


class PokemonType(str, enum.Enum):
    ALL_ROUNDER = "ALL_ROUNDER"
    ATTACKER = "ATTACKER"
    DEFENDER = "DEFENDER"
    SPEEDSTER = "SPEEDSTER"
    SUPPORTER = "SUPPORTER"


class PokemonDifficulty(str, enum.Enum):
    NOVICE = "NOVICE"
    INTERMEDIATE = "INTERMEDIATE"
    EXPERT = "EXPERT"


class AttackType(str, enum.Enum):
    SPECIAL = "SPECIAL"
    PHYSICAL = "PHYSICAL"


class Stadistics(BaseModel):    
    pokemon_id: int = Field(..., description="Identifier of the Pokemon to which the stadistics belongs to.", example=1)
    offense: float = Field(..., description="Pokémon’s ability to deal damage, determined by its Attack and Special Attack stats.", example=4.5)
    endurance: float = Field(..., description="Pokémon’s ability to receive damage without being knocked out, determined by Defense and base HP stats.", example=5)
    mobility: float = Field(..., description="How quickly a Pokémon can get around the field, either manually with its Speed stat or with its Moves.", example=0)
    scoring: float = Field(..., description="How proficient a Pokémon is at scoring goals, determined by how quickly they get around and how well they can defend themselves in enemy territory.", example=3.5)
    support: float = Field(..., description="Pokémon’s capacity for healing and defending teammates, as well as hindering opponents without directly attacking them.", example=2.5)

    # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
    # (or any other arbitrary object with attributes). So, in will try to read data["id"] and also data.id
    class Config:
        orm_mode = True


class PokemonPrice(BaseModel):
    pokemon_id: int = Field(..., description="Identifier of the Pokemon to which the stadistics belongs to.", example=1)
    aeos_coins: int = Field(..., description="Identifier of the Pokemon to which the stadistics belongs to.", example=10500)
    aeos_gems: int = Field(..., description="Identifier of the Pokemon to which the stadistics belongs to.", example=150)


class SkinBase(BaseModel):
    pokemon_id: int
    image: Optional[str]
    gems_cost: int

class Skin(SkinBase):
    id: int = Field(..., description="Skin's identifier in the database.", example=1)

class SkinCreate(SkinBase):
    pass


class PokemonBase(BaseModel):
    name: str = Field(..., description="Pokemon's name.", example="Pikachu")
    type: PokemonType = Field(..., description="Pokemon's type.", example="ATTACKER")
    difficulty: PokemonDifficulty = Field(..., description="Pokemon's difficulty.", example="NOVICE")
    street: MapStreet = Field(..., description="Best map's street/line to go with the pokemon.", example="TOP")
    attack_type: AttackType = Field(..., description="Pokemon's attack type, in order to know which items fit it best.", example="SPECIAL")
    image: Optional[str] = Field(..., description="Pokemon's image.", example="https://pikachu.jpg")
    video: Optional[str] = Field(..., description="Pokemon's video.", example="https://pikachu.mp4")

class Pokemon(PokemonBase):
    id: int = Field(..., description="Pokemon's identifier in the database.", example=1)
    stadistics: Stadistics
    prices: PokemonPrice
    skins: Optional[List[Skin]]
    moves: Optional[List[Move]]

    # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
    # (or any other arbitrary object with attributes). So, in will try to read data["id"] and also data.id
    class Config:
        orm_mode = True

class PokemonCreate(PokemonBase):
    pass
