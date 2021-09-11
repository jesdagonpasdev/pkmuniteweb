import enum

from typing import List, Optional
from pydantic import BaseModel, Field


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
    BASIC = "BASIC"
    FIRST_SET = "FIRST_SET"
    SECOND_SET = "SECOND_SET"
    UNITE_MOVE = "UNITE_MOVE"
    PASIVE = "PASIVE"


class StadisticsBase(BaseModel):
    offense: float = Field(..., description="Pokémon’s ability to deal damage, determined by its Attack and Special Attack stats.", example=4.5)
    endurance: float = Field(..., description="Pokémon’s ability to receive damage without being knocked out, determined by Defense and base HP stats.", example=5)
    mobility: float = Field(..., description="How quickly a Pokémon can get around the field, either manually with its Speed stat or with its Moves.", example=0)
    scoring: float = Field(..., description="How proficient a Pokémon is at scoring goals, determined by how quickly they get around and how well they can defend themselves in enemy territory.", example=3.5)
    support: float = Field(..., description="Pokémon’s capacity for healing and defending teammates, as well as hindering opponents without directly attacking them.", example=2.5)

class Stadistics(StadisticsBase):    
    pokemon_id: int = Field(..., description="Identifier of the Pokemon to which the stadistics belongs to.", example=1)

    # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
    # (or any other arbitrary object with attributes). So, in will try to read data["id"] and also data.id
    class Config:
        orm_mode = True

class StadisticsCreate(StadisticsBase):
    pass


class PokemonPriceBase(BaseModel):
    aeos_coins: int = Field(..., description="Identifier of the Pokemon to which the stadistics belongs to.", example=10500)
    aeos_gems: int = Field(..., description="Identifier of the Pokemon to which the stadistics belongs to.", example=150)

class PokemonPrice(PokemonPriceBase):
    pokemon_id: int = Field(..., description="Identifier of the Pokemon to which the stadistics belongs to.", example=1)

    # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
    # (or any other arbitrary object with attributes). So, in will try to read data["id"] and also data.id
    class Config:
        orm_mode = True
    
class PokemonPriceCreate(PokemonPriceBase):
    pass


class SkinBase(BaseModel):
    image: Optional[str]
    gems_cost: int

class Skin(SkinBase):
    id: int = Field(..., description="Skin's identifier in the database.", example=1)
    pokemon_id: int

    # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
    # (or any other arbitrary object with attributes). So, in will try to read data["id"] and also data.id
    class Config:
        orm_mode = True

class SkinCreate(SkinBase):
    pass


class MoveBase(BaseModel):
    name: str = Field(..., description="Move's name.", example="Thunder")
    description: Optional[str] = Field(..., description="Move's details.", example="Throw a thunder in an area that stun the enemies.")
    type: MoveType  = Field(..., description="Move's type.", example="AREA")
    image: Optional[str] = Field(..., description="Move's image.", example="https://thunder.jpg")
    level: int = Field(..., description="Level to which the pokemon learn the move.", example=6)
    set: MoveSet = Field(..., description="Set to which the move belongs to.", example="FIRST_SET")
    cool_down: int = Field(..., description="Time, in second, to use the move again.", example=8)

class Move(MoveBase):
    id: int = Field(..., description="Move's identifier in the database.", example=1)    
    pokemon_id: int = Field(..., description="Identifier of the Pokemon to which the move belongs to.", example=1)

    # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
    # (or any other arbitrary object with attributes). So, in will try to read data["id"] and also data.id
    class Config:
        orm_mode = True

class MoveCreate(MoveBase):
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

    stadistics: Optional[Stadistics]
    prices: Optional[PokemonPrice]
    skins: Optional[List[Skin]]
    moves: Optional[List[Move]]

    # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
    # (or any other arbitrary object with attributes). So, in will try to read data["id"] and also data.id
    class Config:
        orm_mode = True

class PokemonCreate(PokemonBase):
    stadistics: Optional[StadisticsCreate]
    prices: Optional[PokemonPriceCreate]
    skins: Optional[List[SkinCreate]]
    moves: Optional[List[MoveCreate]]
