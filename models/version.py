from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Version(Base):
    __tablename__ = "tbl_version"

    ID_version = Column(Integer, primary_key=True, autoincrement=True)
    id_product = Column(String, unique=True)
    release_notes = Column(String)
