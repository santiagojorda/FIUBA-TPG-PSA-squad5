from sqlalchemy import Column, Integer, String , Date, ForeignKey, PrimaryKeyConstraint
from pydantic import BaseModel, Optional
from datetime import date

from res.base import Base
from models.version import Version
from models.product import Product

TABLE_NAME = "tbl_ticket"
ID_COLUMN_NAME = "id"   

class TicketModel(BaseModel):
    product_id: int
    version_code: str
    title: str
    description: str
    state: str
    opening_date: date
    opening_date: Optional[date] = None 
    client_id: int
    employee_id: int

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

    __table_args__ = (
        PrimaryKeyConstraint("id", "version_code", "product_id"),
    )

    @staticmethod
    def getIDTableAndColumnName():
        return f"{TABLE_NAME}.{ID_COLUMN_NAME}"

