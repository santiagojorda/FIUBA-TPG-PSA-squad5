from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
TABLE_NAME = "tbl_incident"

ID_COLUMN_NAME = "id"
DURATION_COLUMN_NAME = "duration"
RESPONSE_TIME_COLUMN_NAME = "response_time"
STEPS_PLAYBACK_COLUMN_NAME = "steps_playback"

class Incidente(Base):
    __tablename__ = TABLE_NAME
    
    ID_incident = Column(Integer, name=ID_COLUMN_NAME, primary_key=True, autoincrement=True)
    ID_ticket = Column(Integer)
    ID_version = Column(Integer)
    ID_proyect = Column(Integer)
    
    # CAMBIAR NOMBRES
    steps_playback = Column(Integer)
    duration = Column(Integer)
    response_time = Column(Integer)


    def __str__(self):
        return f"id_task:"
