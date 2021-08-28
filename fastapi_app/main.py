from typing import List
from fastapi import Depends, FastAPI, HTTPException

from sqlmodel import SQLModel

from fastapi_app import schemas
from fastapi_app.crud import map as map_crud
from fastapi_app.database import models
from fastapi_app.database.database import engine


# It is important to import our models before our engine and import models and engine before call this function.
# Otherwise this function is NOT going to create the tables that we has specified in our models.
SQLModel.metadata.create_all(engine)

app = FastAPI()

# Maps
@app.get(
    "/maps/",
    response_model=List[models.Map],
    responses=schemas.ErrorResponses(),
    description="Get all the information of all Maps.",
    summary="Get all the Maps.")
def read_maps(skip: int = 0, limit: int = 100):
    maps = []
    return map_crud.get_maps(skip=skip, limit=limit)

"""
@app.get(
    "/maps/{map_id}",
    response_model=schemas.Map,
    responses=schemas.ErrorResponses(),
    description="Get all the information of the wanted Map.",
    summary="Get the wanted Map."
)
def read_map(map_id: int, db: Session = Depends(get_db)):
    db_map = map_crud.get_map(db, map_id=map_id)
    if db_map is None:
        raise HTTPException(status_code=404, detail="Map not found")
    return db_map


@app.post(
    "/maps/",
    response_model=schemas.Map,
    responses=schemas.ErrorResponses(),
    description="Create a Map with the received information.",
    summary="Create a Map."
)
def create_map(map: schemas.MapCreate, db: Session = Depends(get_db)):
    db_map = map_crud.get_map_by_attributes(db, map=map)
    if db_map:
        raise HTTPException(status_code=400, detail="Map already registered")
    return map_crud.create_map(db=db, map=map)
 """
