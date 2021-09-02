from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from fastapi_app.crud import map as map_crud
from fastapi_app.crud import item as item_crud
from fastapi_app.database.database import SessionLocal, engine

from fastapi_app import schemas
from fastapi_app.database.database import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
# We are creating the database session before each request in the dependency with yield, and then closing it afterwards.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Maps
@app.get(
    "/maps/",
    response_model=List[schemas.Map],
    responses=schemas.ErrorResponses(),
    description="Get all the information of all Maps.",
    summary="Get all the Maps.")
def read_maps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    maps = map_crud.get_maps(db, skip=skip, limit=limit)
    return maps


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


# Item
@app.get(
    "/items/",
    response_model=List[schemas.Item],
    responses=schemas.ErrorResponses(),
    description="Get all the information of all Items.",
    summary="Get all the Items.")
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = item_crud.get_items(db, skip=skip, limit=limit)
    return items


@app.get(
    "/items/{item_id}",
    response_model=schemas.Item,
    responses=schemas.ErrorResponses(),
    description="Get all the information of the wanted Item.",
    summary="Get the wanted Item."
)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = item_crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.patch(
    "/items/{item_id}",
    response_model=schemas.Item
)
async def update_item(item: schemas.Item, db: Session = Depends(get_db)):
    update_item = item_crud.update_item(db, item=item)
    return update_item


@app.post(
    "/items/",
    response_model=schemas.Item,
    responses=schemas.ErrorResponses(),
    description="Create an Item with the received information.",
    summary="Create an Item."
)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = item_crud.get_item_by_attributes(db, item=item)
    if db_item:
        raise HTTPException(status_code=400, detail="Item already registered.")
    return item_crud.create_item(db=db, item=item)


@app.delete(
    "/items/{item_id}",
    description="Delete all the information of the selected Item.",
    summary="Delete the selected Item."
)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    result = item_crud.delete_item(db, item_id=item_id)
    if result == 0:
        raise HTTPException(status_code=400, detail="Item not registered.")
    else:
        return True


# Pokemon
@app.get(
    "/pokemons/",
    response_model=List[schemas.Pokemon],
    responses=schemas.ErrorResponses(),
    description="Get all the information of all Items.",
    summary="Get all the Items.")
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = item_crud.get_items(db, skip=skip, limit=limit)
    return items


@app.get(
    "/items/{item_id}",
    response_model=schemas.Item,
    responses=schemas.ErrorResponses(),
    description="Get all the information of the wanted Item.",
    summary="Get the wanted Item."
)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = item_crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.patch(
    "/items/{item_id}",
    response_model=schemas.Item
)
async def update_item(item: schemas.Item, db: Session = Depends(get_db)):
    update_item = item_crud.update_item(db, item=item)
    return update_item


@app.post(
    "/items/",
    response_model=schemas.Item,
    responses=schemas.ErrorResponses(),
    description="Create an Item with the received information.",
    summary="Create an Item."
)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = item_crud.get_item_by_attributes(db, item=item)
    if db_item:
        raise HTTPException(status_code=400, detail="Item already registered.")
    return item_crud.create_item(db=db, item=item)


@app.delete(
    "/items/{item_id}",
    description="Delete all the information of the selected Item.",
    summary="Delete the selected Item."
)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    result = item_crud.delete_item(db, item_id=item_id)
    if result == 0:
        raise HTTPException(status_code=400, detail="Item not registered.")
    else:
        return True