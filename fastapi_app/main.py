from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from fastapi_app.crud import map as map_crud
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


@app.get("/maps/", response_model=List[schemas.Map], responses=schemas.ErrorResponses())
def read_maps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    maps = map_crud.get_maps(db, skip=skip, limit=limit)
    return maps


@app.get("/maps/{map_id}", response_model=schemas.Map, responses=schemas.ErrorResponses())
def read_user(map_id: int, db: Session = Depends(get_db)):
    db_map = map_crud.get_map(db, map_id=map_id)
    if db_map is None:
        raise HTTPException(status_code=404, detail="Map not found")
    return db_map


@app.post("/maps/", response_model=schemas.Map, responses=schemas.ErrorResponses())
def create_map(map: schemas.MapCreate, db: Session = Depends(get_db)):
    db_map = map_crud.get_map_by_attributes(db, map=map)
    if db_map:
        raise HTTPException(status_code=400, detail='Map already registered')
    return map_crud.create_map(db=db, map=map)
