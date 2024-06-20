# my_fastapi_app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.product import Base as Base_product 
from models.ticket import Base as Base_ticket
from models.version import Base as Base_version
from models.consulta import Base as Base_consulta
from models.incidente import Base as Base_incidente
from models.incidente_por_tarea import Base as Base_incidente_por_tarea

SQLALCHEMY_DATABASE_URL = "sqlite:///soporte.db"

class Database: 
    def __init__(self, db_url): 
        self.engine = create_engine(db_url, echo=True)
        self.Session = sessionmaker(bind=self.engine)

        Base_ticket.metadata.create_all(bind=self.engine)
        Base_product.metadata.create_all(bind=self.engine)
        Base_version.metadata.create_all(bind=self.engine)
        Base_consulta.metadata.create_all(bind=self.engine)
        Base_incidente.metadata.create_all(bind=self.engine)
        Base_incidente_por_tarea.metadata.create_all(bind=self.engine)

    def get_session(self):
        return self.Session()



db = Database(SQLALCHEMY_DATABASE_URL)  #singleton
