from pydantic import BaseModel
class Product(BaseModel):
    id:int
    Name:str
    price:int
    quantitiy:int
