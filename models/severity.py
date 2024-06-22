from sqlalchemy import Column, Integer 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
TABLE_NAME = "tbl_severity"

ID_COLUMN_NAME = "id"
RESPONSE_TIME_COLUMN_NAME = "response_time"

class Severity(Base):
    __tablename__ = TABLE_NAME

    id_severity = Column(Integer, name=ID_COLUMN_NAME, primary_key=True, autoincrement=True)
    response_time = Column(Integer, name=RESPONSE_TIME_COLUMN_NAME, unique=True)

    def __str__(self):
        return f""
