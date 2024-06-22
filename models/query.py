from sqlalchemy import Column, Integer, String , Date

from res.base import Base

TABLE_NAME = "tbl_query"

class Query(Base):
    __tablename__ = TABLE_NAME
    ID_Consulta = Column(Integer, primary_key=True, autoincrement=True)
    ID_ticket = Column(Integer)
    ID_version = Column(Integer)
    ID_proyect = Column(Integer)
    response = Column(String)
