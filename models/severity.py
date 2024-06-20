from sqlalchemy import Column, Integer 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Severity(Base):
    __tablename__ = "tbl_severity"

    id_severity = Column(Integer, primary_key=True, autoincrement=True)
    response_time = Column(Integer, unique=True)

    def __str__(self):
        return f""
