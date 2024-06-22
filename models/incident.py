from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint

from res.base import Base

from models.ticket import Ticket
from models.product import Product
from models.version import Version

TABLE_NAME = "tbl_incident"

class Incident(Base):
    __tablename__ = TABLE_NAME
    
    ticket_id = Column(Integer, ForeignKey(Ticket.getIDTableAndColumnName()))
    product_id = Column(Integer, ForeignKey(Product.getIDTableAndColumnName()))
    version_code = Column(Integer, ForeignKey(Version.getVersionCodeTableAndColumnName()))
    
    # CAMBIAR NOMBRES
    playback_steps = Column(Integer)
    duration = Column(Integer)
    response_time = Column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint("ticket_id", "version_code", "product_id"),
    )