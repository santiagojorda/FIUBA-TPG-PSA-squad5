from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "tbl_product"

    ID_product = Column(Integer, primary_key=True, autoincrement=True)
    
    title = Column(String, unique=True)
