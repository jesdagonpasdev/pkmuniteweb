from sqlalchemy.orm import Session

from fastapi_app import schemas
from fastapi_app.database import models


def get_map(db: Session, map_id: int):
    return db.query(models.Map).filter(models.Map.id == map_id).first()


def get_map_by_attributes(db: Session, map: schemas.MapCreate):
    return db.query(models.Map).filter(
        models.Map.name == map.name, 
        models.Map.players == map.players, 
        models.Map.battle_time == map.battle_time, 
        models.Map.battle_mode == map.battle_mode
    ).first()


def get_maps(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Map).offset(skip).limit(limit).all()


def create_map(db: Session, map: schemas.MapCreate):
    db_map = models.Map(
        name=map.name,
        image=map.image,
        players=map.players,
        battle_time=map.battle_time,
        battle_mode=map.battle_mode,
    )
    db.add(db_map)
    db.commit()
    db.refresh(db_map)
    db_map.battle_mode = db_map.battle_mode.value
    return db_map