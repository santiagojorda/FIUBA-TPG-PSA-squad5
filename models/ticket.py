from sqlalchemy import Column, Integer, String , Date 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ticket(Base):
    __tablename__ = "tbl_tickets"

    id = Column(Integer, primary_key=True, autoincrement=True)

    id_proyect = Column(Integer)
    id_version = Column(Integer)

    title = Column(String(50))
    description = Column(String(200))
    state = Column(String(25))
    closing_date = Column(Date)
    opening_date = Column(Date)

    def __str__(self):
        return f""
