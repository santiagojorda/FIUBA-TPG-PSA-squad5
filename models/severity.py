from sqlalchemy import Column, Integer 
from sqlalchemy.ext.declarative import declarative_base

from res.base import Base

TABLE_NAME = "tbl_severity"
ID_COLUMN_NAME = "id"

S1_RESPONSE_TIME = 14
S2_RESPONSE_TIME = 30
S3_RESPONSE_TIME = 90
S4_RESPONSE_TIME = 365

class Severity(Base):
    __tablename__ = TABLE_NAME

    id = Column(Integer, name=ID_COLUMN_NAME, primary_key=True, autoincrement=True)
    response_time = Column(Integer, unique=True)

    @staticmethod
    def getIDTableAndColumnName():
        return f"{TABLE_NAME}.{ID_COLUMN_NAME}"
