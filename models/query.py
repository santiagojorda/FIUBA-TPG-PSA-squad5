from sqlalchemy import Column, Integer, String , ForeignKey, PrimaryKeyConstraint

from models.ticket import Ticket
from models.product import Product
from models.version import Version

from res.base import Base

TABLE_NAME = "tbl_query"

class Query(Base):
    __tablename__ = TABLE_NAME

    ticket_id = Column(Integer, ForeignKey(Ticket.getIDTableAndColumnName()))
    product_id = Column(Integer, ForeignKey(Product.getIDTableAndColumnName()))
    version_code = Column(Integer, ForeignKey(Version.getVersionCodeTableAndColumnName()))
    response = Column(String(1000), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("ticket_id", "version_code", "product_id"),
    )