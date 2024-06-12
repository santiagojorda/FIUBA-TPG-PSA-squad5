from sqlalchemy import Column, Integer, String
from res.database import Base

class Ticket(Base):
    __tablename__ = "tbl_tickets"

    ID_ticket = Column(Integer, primary_key=True, index=True)
    version_number = Column(String, unique=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    state = Column(String, index=True)