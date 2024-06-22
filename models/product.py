from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
TABLE_NAME = "tbl_product"

ID_COLUMN_NAME = "id"
TITLE_COLUMN_NAME = "title"

class Product(Base):
    __tablename__ = TABLE_NAME

    id = Column(ID_COLUMN_NAME, Integer, primary_key=True, autoincrement=True)
    title = Column(TITLE_COLUMN_NAME, String(100), unique=True)
    
    @staticmethod
    def getIDColumnName():
        return f"{TABLE_NAME}.{ID_COLUMN_NAME}"