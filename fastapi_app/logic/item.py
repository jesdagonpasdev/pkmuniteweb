from fastapi_app import schemas
from fastapi_app.database import models

def ItemUpdate(db_item: models.Item, item: schemas.Item):
    if db_item.name != item.name:
        db_item.name = item.name
    if db_item.image != item.image:
        db_item.image = item.image
    if db_item.description != item.description:
        db_item.description = item.description
    if db_item.summary != item.summary:
        db_item.summary = item.summary
    if db_item.type != item.type:
        db_item.type = item.type
    return db_item