from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint

from res.base import Base

from models.ticket import Ticket, TicketModel
from models.product import Product
from models.version import Version
from models.severity import Severity

TABLE_NAME = "tbl_incident"

class IncidentModel(TicketModel):
    severity_id: int
    playback_steps: str
    duration: int

# class Incident(Base):
#     __tablename__ = TABLE_NAME
    
#     ticket_id = Column(Integer, ForeignKey(Ticket.getIDTableAndColumnName()))
#     product_id = Column(Integer, ForeignKey(Product.getIDTableAndColumnName()))
#     version_code = Column(Integer, ForeignKey(Version.getVersionCodeTableAndColumnName())) 
#     severity_id = Column(Integer, ForeignKey(Severity.getIDTableAndColumnName()))

#     playback_steps = Column(String(1000), nullable=False)
#     duration = Column(Integer, nullable=False)
#     # response_time = Column(Integer)

#     __table_args__ = (
#         PrimaryKeyConstraint("ticket_id", "version_code", "product_id"),
#     )