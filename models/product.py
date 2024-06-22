from sqlalchemy import Column, Integer, String

from res.base import Base

TABLE_NAME = "tbl_product"
ID_COLUMN_NAME = "id"

class Product(Base):
    __tablename__ = TABLE_NAME

    id = Column(Integer, name=ID_COLUMN_NAME, primary_key=True, autoincrement=True)
    title = Column(String(100), unique=True)

    @staticmethod
    def getIDTableAndColumnName():
        return f"{TABLE_NAME}.{ID_COLUMN_NAME}"