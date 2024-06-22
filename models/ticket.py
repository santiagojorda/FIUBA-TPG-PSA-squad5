from sqlalchemy import Column, Integer, String , Date, ForeignKey, PrimaryKeyConstraint

from res.base import Base
from models.version import Version
from models.product import Product

TABLE_NAME = "tbl_ticket"
ID_COLUMN_NAME = "id"

class Ticket(Base):
    __tablename__ = TABLE_NAME

    id = Column(Integer, name=ID_COLUMN_NAME, primary_key=True) # tenemos que manejar el id desde el servicio max de la tupla

    id_product = Column(Integer, ForeignKey(Product.getIDTableAndColumnName()))
    version_code = Column(Integer, ForeignKey(Version.getVersionCodeTableAndColumnName()))

    title = Column(String(50))
    description = Column(String(200))
    state = Column(String(25))
    closing_date = Column(Date)
    opening_date = Column(Date)
    client_id = Column(Date)
    employee_id = Column(Date)

    __table_args__ = (
        PrimaryKeyConstraint("id", "version_code", "id_product"),
    )

    @staticmethod
    def getIDTableAndColumnName():
        return f"{TABLE_NAME}.{ID_COLUMN_NAME}"

