from sqlalchemy import Column, Integer 
from sqlalchemy.ext.declarative import declarative_base

from res.base import Base

TABLE_NAME = "tbl_severity"

class Severity(Base):
    __tablename__ = TABLE_NAME

    id = Column(Integer, primary_key=True, autoincrement=True)
    response_time = Column(Integer, unique=True)
