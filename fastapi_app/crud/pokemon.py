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

def create_stadistics(db: Session, stadistics: schemas.StadisticsCreate, pokemon_id: int):
    db_stadistics = models.Stadistics(**stadistics.dict(), pokemon_id=pokemon_id)
    db.add(db_stadistics)
    db.commit()
    db.refresh(db_stadistics)
    return db_stadistics

def create_prices(db: Session, prices: schemas.PokemonPriceCreate, pokemon_id: int):
    db_prices = models.PokemonPrice(**prices.dict(), pokemon_id=pokemon_id)
    db.add(db_prices)
    db.commit()
    db.refresh(db_prices)
    return db_prices

def create_skin(db: Session, skin: schemas.StadisticsCreate, pokemon_id: int):
    db_skin = models.Skin(**skin.dict(), pokemon_id=pokemon_id)
    db.add(db_skin)
    db.commit()
    db.refresh(db_skin)
    return db_skin

def create_move(db: Session, move: schemas.StadisticsCreate, pokemon_id: int):
    db_move = models.Move(**move.dict(), pokemon_id=pokemon_id)
    db.add(db_move)
    db.commit()
    db.refresh(db_move)
    return db_move
    


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
def update_pokemon(db: Session, pokemon: schemas.Pokemon, pokemon_to_update: schemas.Pokemon):
    # Update model class variable from requested fields
    pokemon_to_update.name = pokemon.name if pokemon.name is not None else pokemon_to_update.name
    pokemon_to_update.type = pokemon.type if pokemon.type is not None else pokemon_to_update.type
    pokemon_to_update.difficulty = pokemon.difficulty if pokemon.difficulty is not None else pokemon_to_update.difficulty
    pokemon_to_update.street = pokemon.street if pokemon.street is not None else pokemon_to_update.street
    pokemon_to_update.attack_type = pokemon.attack_type if pokemon.attack_type is not None else pokemon_to_update.attack_type
    pokemon_to_update.image = pokemon.image if pokemon.image is not None else pokemon_to_update.image
    pokemon_to_update.video = pokemon.video if pokemon.video is not None else pokemon_to_update.video

    db.commit()
    return pokemon_to_update

def update_stadistics(db: Session, stadistics: schemas.Pokemon, stadistics_to_update: schemas.Pokemon):
    # Update model class variable from requested fields
    stadistics_to_update.offense = stadistics.offense if stadistics.offense is not None else stadistics_to_update.offense
    stadistics_to_update.endurance = stadistics.endurance if stadistics.endurance is not None else stadistics_to_update.endurance
    stadistics_to_update.mobility = stadistics.mobility if stadistics.mobility is not None else stadistics_to_update.mobility
    stadistics_to_update.scoring = stadistics.scoring if stadistics.scoring is not None else stadistics_to_update.scoring
    stadistics_to_update.support = stadistics.support if stadistics.support is not None else stadistics_to_update.support

    db.commit()
    return stadistics_to_update

def update_prices(db: Session, pokemon: schemas.Pokemon, pokemon_to_update: schemas.Pokemon):
    # Update model class variable from requested fields
    pokemon_to_update.name = pokemon.name if pokemon.name is not None else pokemon_to_update.name
    pokemon_to_update.type = pokemon.type if pokemon.type is not None else pokemon_to_update.type
    pokemon_to_update.difficulty = pokemon.difficulty if pokemon.difficulty is not None else pokemon_to_update.difficulty
    pokemon_to_update.street = pokemon.street if pokemon.street is not None else pokemon_to_update.street
    pokemon_to_update.attack_type = pokemon.attack_type if pokemon.attack_type is not None else pokemon_to_update.attack_type
    pokemon_to_update.image = pokemon.image if pokemon.image is not None else pokemon_to_update.image
    pokemon_to_update.video = pokemon.video if pokemon.video is not None else pokemon_to_update.video

    db.commit()
    return pokemon_to_update

def update_skin(db: Session, pokemon: schemas.Pokemon, pokemon_to_update: schemas.Pokemon):
    # Update model class variable from requested fields
    pokemon_to_update.name = pokemon.name if pokemon.name is not None else pokemon_to_update.name
    pokemon_to_update.type = pokemon.type if pokemon.type is not None else pokemon_to_update.type
    pokemon_to_update.difficulty = pokemon.difficulty if pokemon.difficulty is not None else pokemon_to_update.difficulty
    pokemon_to_update.street = pokemon.street if pokemon.street is not None else pokemon_to_update.street
    pokemon_to_update.attack_type = pokemon.attack_type if pokemon.attack_type is not None else pokemon_to_update.attack_type
    pokemon_to_update.image = pokemon.image if pokemon.image is not None else pokemon_to_update.image
    pokemon_to_update.video = pokemon.video if pokemon.video is not None else pokemon_to_update.video

    db.commit()
    return pokemon_to_update

def update_move(db: Session, pokemon: schemas.Pokemon, pokemon_to_update: schemas.Pokemon):
    # Update model class variable from requested fields
    pokemon_to_update.name = pokemon.name if pokemon.name is not None else pokemon_to_update.name
    pokemon_to_update.type = pokemon.type if pokemon.type is not None else pokemon_to_update.type
    pokemon_to_update.difficulty = pokemon.difficulty if pokemon.difficulty is not None else pokemon_to_update.difficulty
    pokemon_to_update.street = pokemon.street if pokemon.street is not None else pokemon_to_update.street
    pokemon_to_update.attack_type = pokemon.attack_type if pokemon.attack_type is not None else pokemon_to_update.attack_type
    pokemon_to_update.image = pokemon.image if pokemon.image is not None else pokemon_to_update.image
    pokemon_to_update.video = pokemon.video if pokemon.video is not None else pokemon_to_update.video

    db.commit()
    return pokemon_to_update



# DELETE
def delete_pokemon(db: Session, pokemon_id: int):
    db_pokemon = db.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()
    if db_pokemon is None:
        return 0
    else:
        db.delete(db_pokemon)
        db.commit()
        return 1
