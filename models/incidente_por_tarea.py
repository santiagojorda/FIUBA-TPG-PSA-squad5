from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Incidente_por_tarea(Base):
    __tablename__ = "tbl_incidente_por_tarea"
    ID_incidente_por_tarea = Column(Integer, primary_key=True, autoincrement=True)
    
    ID_task = Column(Integer)
    ID_proyect = Column(Integer)
    ID_ticket = Column(Integer)
    ID_version = Column(Integer)
    Id_product = Column(Integer)

    def __str__(self):
        return f"id_task: {self.id_task}, id_ticket: {self.ID_ticket}, id_version: {self.ID_version}, id_proyect: {self.ID_proyect}, id_product: {self.Id_product}"
