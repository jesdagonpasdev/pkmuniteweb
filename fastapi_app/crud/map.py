from sqlmodel import Session, select

from fastapi_app.database import models
from fastapi_app.database.database import engine


def get_map(map_id: int):
    with Session(engine) as session:
        map = session.exec(select(models.Map).where(models.Map.id == map_id)).first()
    return map


def get_map_by_attributes(map: models.Map):
    with Session(engine) as session:
        map = session.exec(select(models.Map).where(
            models.Map.name == map.name,
            models.Map.players == map.players,
            models.Map.battle_time == map.battle_time,
            models.Map.battle_mode == map.battle_mode
        )).first()
    return map


def get_maps(skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        # We have to call the all() method in order to return a list with all the objects.
        # Without all() we have got an iterable, but not a list.
        maps = session.exec(select(models.Map).offset(skip).limit(limit)).all()
    return maps


def create_map(map: models.Map):
    new_map = models.Map(
        name=map.name,
        image=map.image,
        players=map.players,
        battle_time=map.battle_time,
        battle_mode=map.battle_mode,
    )

    # Use a with block to create a Session using the engine.
    with Session(engine) as session:
        session.add(new_map)
        session.commit()
        session.refresh(new_map)

    return new_map
