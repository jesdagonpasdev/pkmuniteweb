from sqlalchemy.orm import Session

from fastapi.encoders import jsonable_encoder

from fastapi_app import schemas
from fastapi_app.database import models


# CREATE

def create_attribute(db: Session, attribute: schemas.AttributeCreate):
    db_attribute = models.Attribute(
        name=attribute.name,
        description=attribute.description,
        min_value=attribute.min_value,
        max_value=attribute.max_value,
        item_id=attribute.item_id
    )
    db.add(db_attribute)
    db.commit()
    db.refresh(db_attribute)
    return db_attribute


# READ

def get_attributes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Attribute).offset(skip).limit(limit).all()


def get_attribute(db: Session, attribute_id: int):
    return db.query(models.Attribute).filter(models.Attribute.id == attribute_id).first()


def get_item_by_attributes(db: Session, attribute: schemas.AttributeCreate):
    return db.query(models.Attribute).filter(
        models.Attribute.item_id == attribute.item_id
    ).first()


# UPDATE

def update_attribute(db: Session, attribute: schemas.Attribute):
    db_attribute = db.query(models.Attribute).filter(models.Attribute.id == attribute.id).first()
    model_attribute = schemas.AttributeCreate(
        name=attribute.name,
        description=attribute.description,
        min_value=attribute.min_value,
        max_value=attribute.max_value,
        item_id=attribute.item_id
    )
    update_data = attribute.dict(exclude_unset=True)
    update_attribute = model_attribute.copy(update=update_data)
    db_attribute = jsonable_encoder(update_attribute)
    return update_attribute


# DELETE

def delete_attribute(db: Session, attribute_id: int):
    db_attribute = db.query(models.Attribute).filter(models.Attribute.id == attribute_id).first()
    if db_attribute is None:
        return 0
    else:
        db.delete(db_attribute)
        db.commit()
        return 1