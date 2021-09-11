from sqlalchemy.orm import Session

from fastapi_app import schemas
from fastapi_app.crud import pokemon as pokemon_crud

class PokemonAlreadyExist(Exception):
    pass

def pokemon_create(db: Session, pokemon: schemas.PokemonCreate):
    existed_pokemon = pokemon_crud.get_pokemon_by_attributes(pokemon=pokemon)
    if existed_pokemon:
        raise PokemonAlreadyExist
    
    created_pokemon = pokemon_crud.create_pokemon(db=db, pokemon=pokemon)

    stadistics = pokemon.stadistics
    stadistics.pokemon_id = created_pokemon.id
    pokemon_crud.create_stadistics(db=db, stadistics=stadistics)

    return pokemon_crud.get_pokemon(db=db, pokemon_id=created_pokemon.id)