#fastapi dev main.py
from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()


# Модель для валідації даних
class Entity(BaseModel):
    name: str
    price: float


# Маршрут, який приймає дані та валідує їх
@app.post("/entities/")
def create_entity(entity: Entity):
    return entity

@app.get("/entitiesa/")
def read_entity(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/entitiesb/")
def read_entity2(param: int | None = None):
    print(param)
    return param

@app.get("/entities/")
def read(value: int = Query(ge=10, le=100, title="Тестоване значення", description="Тестовий паремтр, перевка в роботі", default=10),
        string: str = Query(title="Пробна строка", description="Перевірка використання рядку", min_length=7, max_length=15),
        listing: list = Query(title="LIST", description="Try to use lists", min_items=1, max_items=3)):
    return {"value": value, "string": string, "listing": listing}


@app.get("/entitiess/")
def read(
    value: Annotated[ 
    int,
    Query(ge=10, le=100, title='val-val',
    description='It`s very important value')
    ] = None
    ):
    return {"value": value}


from fastapi import Path, Body

@app.get("/entities/{entity_id}")
def read(
    entity_id: int = Path(ge=10, le=100, title='entity_id',
    description='It`s very important value'), 
    query_param: str = Query(title="Query Parameter", 
    description="Additional query parameter")
    ):
    return {"entity_id": entity_id, "query_param": query_param}


@app.post("/entity/")
def update_item(
    entity: Entity, add_body: Annotated[int, Body()]):
    pass


from pydantic import Field


class Entity(BaseModel):
    id: int = 1
    value: str | None = Field(
    default=None, min_length=10, 
    max_length=50)

@app.post("/entities/")
def read(entity: Entity | None):
    return {"entity_id": entity.id, "entity_val": 
    entity.value}


from fastapi.templating import Jinja2Templates
from starlette.requests import Request

# Вказуємо шаблони Jinja2
templates = Jinja2Templates(directory="templates")
# Головна сторінка
@app.get("/")
def read_root(request: Request):
    # Дані, які будуть передані в шаблон
    data = {"message": "Hello, World!"}

    # Відображення сторінки з використанням Jinja2
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

# from fastapi.staticfiles import StaticFiles

# app.mount("/templates/static", StaticFiles(directory="static"), 
# name="static")