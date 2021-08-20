from typing import Optional

from fastapi import FastAPI

app = FastAPI(title='Prueba',
              description='Prueba de FastAPI',
              version='1.0.0')


@app.get("/")
async def index():
    return {"Hello": "World"}

@app.get("/news")
async def news():
    return 'Estamos en la pestaña de Noticias'

@app.get("/pokemon")
async def pokemon():
    return 'Estamos en la pestaña de Pokemon'

@app.get("/items")
async def pokemon():
    return 'Estamos en la pestaña de Items'

@app.get("/maps")
async def maps():
    return 'Estamos en la pestaña de Maps'

@app.get("/builds")
async def builds():
    return 'Estamos en la pestaña de Builds'

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}