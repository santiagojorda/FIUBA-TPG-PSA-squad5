from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.schema import PrimaryKeyConstraint

from models.product import Product
from res.base import Base

TABLE_NAME = "tbl_version"
CODE_COLUMN_NAME = "version_code"
RELEASE_NOTES_COLUMN_NAME = "release_notes"

class Version(Base):
    __tablename__ = TABLE_NAME

    version_code = Column(String(11), name=CODE_COLUMN_NAME, primary_key=True)
    id_product = Column(Integer, ForeignKey(Product.getIDColumnName()))

    release_notes = Column(String(300), name=RELEASE_NOTES_COLUMN_NAME)

    __table_args__ = (
        PrimaryKeyConstraint("version_code", "id_product"),
    )
    
    @staticmethod
    def getVersionColumn():
        return f"{TABLE_NAME}.{CODE_COLUMN_NAME}"