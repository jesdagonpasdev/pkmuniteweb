from pydantic import BaseModel, Field


class Attribute(BaseModel):
    id: int = Field(..., description="Attribute's identifier in the database.", example=1)
    name: str = Field(..., description="Attribute's name.", example="HP")
    description: str = Field(..., description="Attribute's description.", example="Maximum Health Points.")
    min_value: int = Field(..., description="Attribute's min value.", example="16.")
    max_value: int = Field(..., description="Attribute's max value.", example="160")
    item_id: int = Field(None, description="Image of the item.", example="2")

# Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
    # (or any other arbitrary object with attributes). So, in will try to read data["id"] and also data.id
    class Config:
        orm_mode = True


class AttributeCreate(BaseModel):
    name: str = Field(..., description="Attribute's name.", example="HP Recovery")
    description: str = Field(..., description="Attribute's description.", example="Restores Health Points each second.")
    min_value: int = Field(..., description="Attribute's min value.", example="0.")
    max_value: int = Field(..., description="Attribute's max value.", example="6")
    item_id: int = Field(None, description="Image of the item.", example="2")