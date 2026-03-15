from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer,Column,String,Float
Base=declarative_base()
class Product(Base):
    __tablename__="Product"
    id=Column(Integer,primary_key=True,index=True)
    Name=Column(String(69),nullable=False)
    price=Column(Float,nullable=False)
    quantitiy=Column(Integer,nullable=False)
