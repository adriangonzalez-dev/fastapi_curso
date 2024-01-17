from typing import Union
from fastapi import FastAPI, HTTPException
from src.models.item_model import Item

app:FastAPI = FastAPI()

items:list[Item] = [
    Item(item_id=1, name="Foo", price=50),
    Item(item_id=2, name="Bar", price=50),
    Item(item_id=3, name="Baz", price=50),
    Item(item_id=4, name="Qux", price=50),
    Item(item_id=8, name="Quux", price=50),
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def get_item_by_id(item_id: int, q:Union[str, None] = None):
    result_items = filter(lambda i:i.item_id == item_id, items)
    #item_id es un req.paramas
    #q es un query param o un None

    if list(result_items) == []:
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found") # raise permite generar un codigo de error http
    return {"item": list(result_items), "query": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item:Item): # Primer argumento params, segundo arg body
    return {"item_name": item.name, "item_id": item_id}
