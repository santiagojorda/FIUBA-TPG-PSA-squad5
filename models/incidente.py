from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Incidente(Base):
    __tablename__ = "tbl_incidente"
    
    ID_incident = Column(Integer, primary_key=True, autoincrement=True)
    ID_ticket = Column(Integer)
    ID_version = Column(Integer)
    ID_proyect = Column(Integer)
    
    # CAMBIAR NOMBRES
    steps_Playback = Column(Integer)
    Impact = Column(String)
    Duration = Column(Integer)
    response_time = Column(Integer)


    def __str__(self):
        return f"id_task: {self.id_task}, id_ticket: {self.ID_ticket}, id_version: {self.ID_version}, id_proyect: {self.ID_proyect}, id_product: {self.Id_product}"
