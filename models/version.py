from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Version(Base):
    __tablename__ = "tbl_version"

    id_version = Column(Integer, primary_key=True, autoincrement=True)
    version_code = Column(String(11))
    id_product = Column(Integer)
    release_notes = Column(String(300))
