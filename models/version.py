from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
TABLE_NAME = "tbl_version"

ID_COLUMN_NAME = "id"
CODE_COLUMN_NAME = "version_code"
RELEASE_NOTES_COLUMN_NAME = "release_notes"

class Version(Base):
    __tablename__ = TABLE_NAME

    id_version = Column(ID_COLUMN_NAME, Integer, primary_key=True, autoincrement=True)
    version_code = Column(CODE_COLUMN_NAME, String(11))
    id_product = Column(Integer)
    release_notes = Column(RELEASE_NOTES_COLUMN_NAME, String(300))
    
    @staticmethod
    def getIDColumnName():
        return f"{TABLE_NAME}.{ID_COLUMN_NAME}"