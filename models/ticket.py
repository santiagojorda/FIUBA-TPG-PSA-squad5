from sqlalchemy import Column, Integer, String , Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.version import Version
from models.product import Product

Base = declarative_base()

TABLE_NAME = "tbl_ticket"
ID_COLUMN_NAME = "id"
TITLE_COLUMN_NAME = "title"
DESCRIPTION_COLUMN_NAME = "description"
STATE_COLUMN_NAME = "state"
CLOSING_DATE_COLUMN_NAME = "closing_date"
OPENING_DATE_COLUMN_NAME = "opening_date"

class Ticket(Base):
    __tablename__ = TABLE_NAME

    id = Column(Integer, name=ID_COLUMN_NAME, primary_key=True, autoincrement=True)

    id_product = Column(Integer, ForeignKey(Product.getIDColumnName()))
    id_version = Column(Integer, ForeignKey(Version.getIDColumnName()))

    title = Column(String(50), name=TITLE_COLUMN_NAME)
    description = Column(String(200), name=DESCRIPTION_COLUMN_NAME)
    state = Column(String(25), name=STATE_COLUMN_NAME)
    closing_date = Column(Date, name=CLOSING_DATE_COLUMN_NAME)
    opening_date = Column(Date, name=OPENING_DATE_COLUMN_NAME)

    product = relationship("Product")
    version = relationship("Version")

    @staticmethod
    def getIDColumnName():
        return f"{TABLE_NAME}.{ID_COLUMN_NAME}"

    def __str__(self):
        return f""
