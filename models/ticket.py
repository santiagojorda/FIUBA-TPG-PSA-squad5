from sqlalchemy import Column, Integer, String , Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.version import Version
from models.proyect import Proyect

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

    id = Column(ID_COLUMN_NAME, Integer, primary_key=True, autoincrement=True)

    id_proyect = Column(Integer, ForeignKey(Proyect.getIDColumnName()))
    id_version = Column(Integer, ForeignKey(Version.getIDColumnName()))

    title = Column(TITLE_COLUMN_NAME, String(50))
    description = Column(DESCRIPTION_COLUMN_NAME, String(200))
    state = Column(STATE_COLUMN_NAME, String(25))
    closing_date = Column(CLOSING_DATE_COLUMN_NAME, Date)
    opening_date = Column(OPENING_DATE_COLUMN_NAME, Date)

    @staticmethod
    def getIDColumnName():
        return f"{TABLE_NAME}.{ID_COLUMN_NAME}"

    def __str__(self):
        return f""
