from sqlalchemy import Column, Integer, PrimaryKeyConstraint, ForeignKey

from res.base import Base

from models.product import Product
from models.ticket import Ticket
from models.version import Version

TABLE_NAME = "tbl_incident_per_task"

class Incident_per_task(Base):
    __tablename__ = TABLE_NAME
    
    task_id = Column(Integer, nullable=False)
    proyect_id = Column(Integer, nullable=False)

    ticket_id = Column(Integer, ForeignKey(Ticket.getIDTableAndColumnName()))
    version_code = Column(Integer, ForeignKey(Version.getVersionCodeTableAndColumnName()))
    product_id = Column(Integer, ForeignKey(Product.getIDTableAndColumnName()))

    __table_args__ = (
        PrimaryKeyConstraint("task_id", "proyect_id", "ticket_id","product_id", "version_code"),
    )