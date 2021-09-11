from sqlalchemy.orm import Session

from fastapi.encoders import jsonable_encoder

from fastapi_app import schemas
from fastapi_app.database import models


# CREATE

def create_pokemon(db: Session, pokemon: schemas.PokemonCreate):
    db_pokemon = models.Pokemon(
        name=pokemon.name,
        type=pokemon.type,
        difficulty=pokemon.difficulty,
        street=pokemon.street,
        attack_type=pokemon.attack_type,
        image=pokemon.image,
        video=pokemon.video
    )
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon

def create_stadistics(db: Session, stadistics: schemas.StadisticsCreate):
    db_stadistics = models.Stadistics(
        pokemon_id=stadistics.pokemon_id,
        offense=stadistics.offense,
        endurance=stadistics.endurance,
        mobility=stadistics.mobility,
        scoring=stadistics.scoring,
        support=stadistics.support
    )
    db.add(db_stadistics)
    db.commit()
    db.refresh(db_stadistics)
    return db_stadistics
    


# READ

def get_pokemons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pokemon).offset(skip).limit(limit).all()


def get_pokemon(db: Session, pokemon_id: int):
    return db.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()


def get_pokemon_by_attributes(db: Session, pokemon: schemas.PokemonCreate):
    return db.query(models.Pokemon).filter(
        models.Pokemon.name == pokemon.name
    ).first()


# UPDATE

def update_pokemon(db: Session, pokemon: schemas.Pokemon):
    model_pokemon = schemas.PokemonCreate(
        name=pokemon.name,
        type=pokemon.type,
        difficulty=pokemon.difficulty,
        street=pokemon.street,
        attack_type=pokemon.attack_type,
        image=pokemon.image,
        video=pokemon.video
    )
    update_data = pokemon.dict(exclude_unset=True)
    update_pokemon = model_pokemon.copy(update=update_data)
    db_pokemon = jsonable_encoder(update_pokemon)
    return update_pokemon


# DELETE

def delete_pokemon(db: Session, pokemon_id: int):
    db_pokemon = db.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()
    if db_pokemon is None:
        return 0
    else:
        db.delete(db_pokemon)
        db.commit()
        return 1