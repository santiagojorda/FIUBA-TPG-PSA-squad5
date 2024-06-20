# my_fastapi_app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.product import Base as BaseProduct 
from models.ticket import Base as BaseTicket
from models.version import Base as BaseVersion

SQLALCHEMY_DATABASE_URL = "sqlite:///soporte.db"

class Database: 
    def __init__(self, db_url): 
        self.engine = create_engine(db_url, echo=True)
        self.Session = sessionmaker(bind=self.engine)

        BaseTicket.metadata.create_all(bind=self.engine)
        BaseProduct.metadata.create_all(bind=self.engine)
        BaseVersion.metadata.create_all(bind=self.engine)

    def get_session(self):
        return self.Session()



db = Database(SQLALCHEMY_DATABASE_URL)  #singleton
