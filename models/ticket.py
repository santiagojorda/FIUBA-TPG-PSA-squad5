from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ticket(Base):
    __tablename__ = "tbl_tickets"

    ID_ticket = Column(Integer, primary_key=True, autoincrement=True)

    ID_proyect = Column(Integer)
    ID_version = Column(Integer)

    title = Column(String(50))
    description = Column(String(200))
    state = Column(String(25))
    closing_date = Column(Date)
    opening_date = Column(Date)

    def __str__(self):
        return f"Titulo: {self.title}, version: {self.version_number}, id: {self.ID_ticket}"
