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
    steps_playback = Column(Integer)
    duration = Column(Integer)
    response_time = Column(Integer)


    def __str__(self):
        return f"id_task:"
