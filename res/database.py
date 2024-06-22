# my_fastapi_app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from res.base import Base

from models.product import Product
from models.version import Version
from models.ticket import Ticket
from models.query import Query
from models.incident import Incident
from models.incident_per_task import Incident_per_task
from models.severity import Severity
# 
SQLALCHEMY_DATABASE_URL = "sqlite:///soporte.db"

class Database(): 
    def __init__(self, db_url): 
        self.engine = create_engine(db_url, echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        Base.metadata.drop_all(bind=self.engine)
        Base.metadata.create_all(bind=self.engine)

        siu = Product(title = "Siu-Gurani")
        self.session.add(siu)

        mercadolibre = Product(title = "MercadoLibre")
        self.session.add(mercadolibre)

        olx = Product(title = "Olx")
        self.session.add(olx)


        siu_version1 = Version(version_code="0.0.0", id_product = 1, release_notes='mi primera version')
        self.session.add(siu_version1)

        siu_version2 = Version(version_code="0.4.0", id_product = 1, release_notes='mi segunda version')
        self.session.add(siu_version2)

        ml_version1 = Version(version_code="4.2.03", id_product = 2, release_notes='mi primera version')
        self.session.add(ml_version1)

        olx_version1 = Version(version_code="2.2.03", id_product = 3, release_notes='mi primera version')
        self.session.add(olx_version1)
        
        # ticket1 = Ticket(
        #     id = 0,
        #     id_product = mercadolibre.id_product,
        #     version_code=
        # )

        # s1 = Severity(response_time = 14)
        # s2 = Severity(response_time = 30)
        # s3 = Severity(response_time = 90)
        # s4 = Severity(response_time = 365)

        # self.session.add(s1)
        # self.session.add(s2)
        # self.session.add(s3)
        # self.session.add(s4)

        self.session.commit()

    def get_session(self):
        return self.session
    
    # def __modulo__(self):
    #     asdasdasda
    #     sdasdasd



db = Database(SQLALCHEMY_DATABASE_URL)  #singleton
