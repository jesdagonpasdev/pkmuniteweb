from sqlalchemy.orm import Session

from fastapi.encoders import jsonable_encoder

from fastapi_app import schemas
from fastapi_app.database import models


# CREATE

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(
        name=item.name,
        image=item.image,
        description=item.description,
        summary=item.summary,
        type=item.type
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db_item.type = db_item.type.value
    return db_item


# READ

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def get_item_by_attributes(db: Session, item: schemas.ItemCreate):
    return db.query(models.Item).filter(
        models.Item.name == item.name,
        models.Item.type == item.type
    ).first()


# UPDATE

def update_item(db: Session, item: schemas.Item):
    db_item = db.query(models.Item).filter(models.Item.id == item.id).first()
    model_item = schemas.ItemCreate(
        name=item.name,
        image=item.image,
        description=item.description,
        summary=item.summary,
        type=item.type
    )
    update_data = item.dict(exclude_unset=True)
    update_item = model_item.copy(update=update_data)
    db_item = jsonable_encoder(update_item)
    return update_item


# DELETE

def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        return 0
    else:
        db.delete(db_item)
        db.commit()
        return 1