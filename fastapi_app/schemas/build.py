import enum

from typing import List, Optional
from pydantic import BaseModel, Field


class MapStreet(str, enum.Enum):
    TOP = "TOP"
    MID = "MID"
    BOTTOM = "BOTTOM"
    ALL = "ALL"


class BuildBase(BaseModel):    
    name: str = Field(..., description="Build's name.", example="Inmortal Snorlax")
    description: str = Field(
        ...,
        description="Build's details.",
        example="Inmortal Snorlax is a build that gives Snorlax extra HPs to make Snorlax's life inexhaustible."
    )
    pokemon_id: int = Field(..., description="Identifier of the Pokemon to which the build belongs to.", example=5)
    held_object_one: int = Field(..., description="Identifier of the held object one.", example=1)
    held_object_two: int = Field(..., description="Identifier of the held object two.", example=2)
    held_object_three: int = Field(..., description="Identifier of the held object three.", example=3)
    battle_object: int = Field(..., description="Identifier of the battle object.", example=2)
    first_movement: int = Field(
        ...,
        description="Identifier of the move that should be taken when the battle starts.",
        example=2
    )
    movement_one: int = Field(..., description="Identifier of the R last move.", example=2)
    movement_two: int = Field(..., description="Identifier of the ZR last move.", example=3)
    tips: Optional[str] = Field(..., description="Useful things that fit well with the build.", example=3)
    street: MapStreet = Field(..., description="Preferable map line to use this build.", example="TOP")


class BuildPartnerBase(BaseModel):
    build_id: int = Field(..., description="Identifier of the Pokemon to which the build belongs to.", example=5)
    pokemon_id: int = Field(..., description="Identifier of the Pokemon that combine well with this build.", example=5)
    description: str = Field(
        ...,
        description="Build Partners's details.",
        example="Pikachu is a good match with Inmortal Snorlax because it could damage the enemies while Snorlax is receiving all the enemies' attacks."
    )


class Build(BuildBase):
    id: int = Field(..., description="Build's identifier in the database.", example=1)
    build_partners: Optional[List[BuildPartnerBase]]

    # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
    # (or any other arbitrary object with attributes). So, in will try to read data["id"] and also data.id
    class Config:
        orm_mode = True


class BuildCreate(BuildBase):
    pass


class BuildPartner(BuildPartnerBase):
    build: Build

    # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
    # (or any other arbitrary object with attributes). So, in will try to read data["id"] and also data.id
    class Config:
        orm_mode = True


class BuildPartnerCreate(BuildPartnerBase):
    pass
