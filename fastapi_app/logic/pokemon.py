from sqlalchemy.orm import Session

from fastapi_app import schemas
from fastapi_app.crud import pokemon as pokemon_crud

class PokemonAlreadyExist(Exception):
    pass

class PokemonCreateException(Exception):
    pass

def pokemon_create(db: Session, pokemon: schemas.PokemonCreate):
    existed_pokemon = pokemon_crud.get_pokemon_by_attributes(db=db, pokemon=pokemon)
    if existed_pokemon:
        raise PokemonAlreadyExist
    
    try:
        created_pokemon = pokemon_crud.create_pokemon(db=db, pokemon=pokemon)

        stadistics = pokemon.stadistics
        pokemon_crud.create_stadistics(db=db, stadistics=stadistics, pokemon_id=created_pokemon.id)

        prices = pokemon.prices
        pokemon_crud.create_prices(db=db, prices=prices, pokemon_id=created_pokemon.id)

        skins = pokemon.skins
        for skin in skins:
            pokemon_crud.create_skin(db=db, skin=skin, pokemon_id=created_pokemon.id)

        moves = pokemon.moves
        for move in moves:
            pokemon_crud.create_move(db=db, move=move, pokemon_id=created_pokemon.id)
    except Exception as Error:
        """ We should delete all the inserted information (transaction effect) """
        pokemon_crud.delete_pokemon(db=db, pokemon_id=created_pokemon.id)
        print(Error)
        raise PokemonCreateException

    return pokemon_crud.get_pokemon(db=db, pokemon_id=created_pokemon.id)


def pokemon_update(db: Session, pokemon: schemas.PokemonCreate):
    pass