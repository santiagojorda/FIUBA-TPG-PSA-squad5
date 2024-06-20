from sqlalchemy import Column, Integer, String , Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Consulta(Base):
    __tablename__ = "tbl_consulta"
    ID_Consulta = Column(Integer, primary_key=True, autoincrement=True)
    ID_ticket = Column(Integer)
    ID_version = Column(Integer)
    ID_proyect = Column(Integer)
    
    answer = Column(String)


    def __str__(self):
        return f"id_task: {self.id_task}, id_ticket: {self.ID_ticket}, id_version: {self.ID_version}, id_proyect: {self.ID_proyect}, id_product: {self.Id_product}"
