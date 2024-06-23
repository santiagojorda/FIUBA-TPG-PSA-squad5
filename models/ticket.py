from sqlalchemy import Column, Integer, String , Date, ForeignKey, PrimaryKeyConstraint
from pydantic import BaseModel
from typing import Optional
from datetime import date

from res.base import Base
from models.version import Version
from models.product import Product
from models.severity import Severity

TABLE_NAME = "tbl_ticket"
ID_COLUMN_NAME = "id"   

class TicketModel(BaseModel):
    product_id: int
    version_code: str
    title: str
    description: str
    state: str
    opening_date: date
    closing_date: Optional[date] = None 
    client_id: int
    employee_id: int

    # Query
    response: Optional[str] = None

    # Incident
    severity_id: Optional[int] = None 
    playback_steps: Optional[str] = None
    duration: Optional[int] = None

class Ticket(Base):
    __tablename__ = TABLE_NAME

    id = Column(Integer, name=ID_COLUMN_NAME) # tenemos que manejar el id desde el servicio max de la tupla

    product_id = Column(Integer, ForeignKey(Product.getIDTableAndColumnName()))
    version_code = Column(Integer, ForeignKey(Version.getVersionCodeTableAndColumnName()))

    title = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)
    state = Column(String(25), nullable=False)
    closing_date = Column(Date) 
    opening_date = Column(Date, nullable=False)
    client_id = Column(Integer, nullable=False)
    employee_id = Column(Integer)

    # query
    response = Column(String(1000))

    # incident
    severity_id = Column(Integer, ForeignKey(Severity.getIDTableAndColumnName()))
    playback_steps = Column(String(1000))
    duration = Column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint("id", "version_code", "product_id"),
    )

    @staticmethod
    def getIDTableAndColumnName():
        return f"{TABLE_NAME}.{ID_COLUMN_NAME}"

