from sqlalchemy import Column, Integer 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
TABLE_NAME = "tbl_severity"

ID_COLUMN_NAME = "id"
RESPONSE_TIME_COLUMN_NAME = "response_time"

class Severity(Base):
    __tablename__ = TABLE_NAME

    id_severity = Column(ID_COLUMN_NAME, Integer, primary_key=True, autoincrement=True)
    response_time = Column(RESPONSE_TIME_COLUMN_NAME, Integer, unique=True)

    def __str__(self):
        return f""
