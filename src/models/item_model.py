from typing import Union
from pydantic import BaseModel

# Se crea un modelo llamado Item
class Item(BaseModel):
    item_id:int
    name:str
    price:float
    is_offer:Union[bool, None] = None