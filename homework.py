#fastapi dev main.py
from fastapi import FastAPI, Query

app = FastAPI()

@app.get('/')
def index():
    return {'Hello Shop!'}

@app.get("/valid_filtr/")
def valid_filtr(
    name : str = Query(title="Name of item", description="Name of item for validation and filtration", min_length=5, max_length=15),
    price : float | int = Query(title="Price of item", description="Price for validation and filtration", ge=10, le=100)):

    return {"name": name, "price": price}