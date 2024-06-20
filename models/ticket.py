from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ticket(Base):
    __tablename__ = "tbl_tickets"

    ID_ticket = Column(Integer, primary_key=True, autoincrement=True)
    version_number = Column(String(20), unique=True)
    title = Column(String(50))
    description = Column(String(200))
    state = Column(String(25))

    

    def __str__(self):
        return f"Titulo: {self.title}, version: {self.version_number}, id: {self.ID_ticket}"
