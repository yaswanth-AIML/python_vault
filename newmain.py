from fastapi import FastAPI,HTTPException,dependencies,Depends
from products import Product
from database import session,engine
import database_models
from sqlalchemy.orm import Session
database_models.Base.metadata.create_all(bind=engine)
app=FastAPI()
products=[
    Product(id=1,Name='laptop',price=999,quantitiy=10),
    Product(id=2,Name='phone',price=9999,quantitiy=3)
]
def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()
def insert_db():
    db=session()
    count=db.query(database_models.Product).count
    if count==0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()
@app.get("/products")
def all_products(db:Session=Depends(get_db)):
    db_products=db.query(database_models.Product).all()
    return db_products
@app.get("/product/{product_id}")
def one_product(product_id:int):
    taken=product_id-1
    if 0<=taken < len(products):
        return products[taken]
    else:
        raise HTTPException(status_code=404,detail="product not found")
@app.post("/product")
def add_product(Product:Product):
    products.append(Product)
    return Product
