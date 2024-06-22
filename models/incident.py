from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from res.base import Base

TABLE_NAME = "tbl_incident"

ID_COLUMN_NAME = "id"
DURATION_COLUMN_NAME = "duration"
RESPONSE_TIME_COLUMN_NAME = "response_time"
STEPS_PLAYBACK_COLUMN_NAME = "steps_playback"

class Incident(Base):
    __tablename__ = TABLE_NAME
    
    ID_incident = Column(Integer, name=ID_COLUMN_NAME, primary_key=True, autoincrement=True)
    ID_ticket = Column(Integer)
    ID_version = Column(Integer)
    ID_proyect = Column(Integer)
    
    # CAMBIAR NOMBRES
    playback_steps = Column(Integer)
    duration = Column(Integer)
    response_time = Column(Integer)