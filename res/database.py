# my_fastapi_app/database.py
from sqlalchemy import create_engine
from datetime import date
from sqlalchemy.orm import sessionmaker
from res.base import Base
from sqlalchemy.sql import func


from models.product import Product
from models.version import Version
from models.ticket import Ticket
from models.query import Query
from models.incident import Incident
from models.incident_per_task import Incident_per_task
from models.severity import Severity
# 
SQLALCHEMY_DATABASE_URL = "sqlite:///sla_support.db"

class Database(): 
    def __init__(self, db_url): 
        self.engine = create_engine(db_url, echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        Base.metadata.drop_all(bind=self.engine)
        Base.metadata.create_all(bind=self.engine)

        self.__initialize_data__()

    def __initialize_data__(self):
        self.__insert_products_and_versions__()
        self.__insert_severities__()


        ticket = Ticket(
            id = 1,
            product_id = 1,
            version_code = '2.2.0',
            title = 'No funca',
            description = 'Descripcion no funciona',
            state = 'Estado 1',
            opening_date = date.today(),
            client_id = 1,
            employee_id = 1
        )
        
        incident = Incident(
            ticket_id = 1,
            product_id = 1,
            version_code = '2.2.0',
            duration = 24,
            playback_steps = 'estos son los pasos a seguir',
            severity_id = 2
        )
        self.session.add(ticket)
        self.session.add(incident)
        self.session.commit()

    def __insert_severities__(self):
        s1 = Severity(response_time = 14)
        s2 = Severity(response_time = 30)
        s3 = Severity(response_time = 90)
        s4 = Severity(response_time = 365)
        self.session.add(s1)
        self.session.add(s2)
        self.session.add(s3)
        self.session.add(s4)

        self.session.commit()
    
    def __insert_products_and_versions__(self):
        siu = Product(title = "Siu-Gurani")
        self.session.add(siu)
        siu_version1 = Version(version_code="1.1.0", product_id = 0, release_notes='mi primera version')
        self.session.add(siu_version1)
        siu_version2 = Version(version_code="2.2.0", product_id = 0, release_notes='mi segunda version')
        self.session.add(siu_version2)

        mercadolibre = Product(title = "MercadoLibre")
        self.session.add(mercadolibre)
        ml_version1 = Version(version_code="4.2.03", product_id = 1, release_notes='mi primera version')
        self.session.add(ml_version1)

        olx = Product(title = "Olx")
        self.session.add(olx)
        olx_version1 = Version(version_code="2.2.03", product_id = 2, release_notes='mi primera version')
        self.session.add(olx_version1)

        self.session.commit()
    
    def get_all_tickets(self):
        return self.session.query(Ticket).all()
    
    # def get_ticket(self, ticket_id: int):
    #     return self.session.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()
    
    def get_query_ticket(self, ticket_id: int):
        query = self.session.query(Query).filter(Query.ticket_id == ticket_id).first()
        return query
    
    def get_ticket(self, ticket_id):
        ticket = self.session.query(Ticket).filter(Ticket.id == ticket_id).first()
        return ticket

    def get_incident_ticket(self, ticket_id: int):
        incident = self.session.query(Incident).filter(Incident.ticket_id == ticket_id).first()
        return incident
    
    def get_severity(self, severity_id: int):
        severity = self.session.query(Severity).filter(Severity.id == severity_id).first()
        return severity
    
    def get_version(self, version_code: int):
        version = self.session.query(Version).filter(Version.version_code == version_code).first()
        return version

    def get_versions_by_product_id(self, product_id: int):
        versions = self.session.query(Version).filter(Version.product_id == product_id).all()    
        return versions

    def get_version_by_product_id(self, product_id, version_code: str):
        version = self.session.filter(Version.product_id == product_id, Version.version_code == version_code).first() 
        return version
    
    def create_ticket(self, ticket_data):
        id = self.session.query(func.max(Ticket.id)).scalar()
        ticket = Ticket(
            id = (id+1),
            title = ticket_data.title,
            description = ticket_data.description,
            client_id = ticket_data.client_id,
            employee_id = ticket_data.employee_id,
            product_id = ticket_data.product_id,
            version_code = ticket_data.version_code,
            opening_date = ticket_data.opening_date,
        )
        self.session.add(ticket)
        self.session.commit()
        return ticket.id

    def create_incident_ticket(self, incident_data):
        incident = Incident(
            ticket_id = incident_data.id,
            client_id = incident_data.client_id,
            product_id = incident_data.product_id,
            version_code = incident_data.version_code,
            duration = incident_data.duration,
            playback_steps = incident_data.playback_steps,
            severity_id = incident_data.severity
        )
        self.session.add(incident)
        self.session.commit()

    # def __modulo__(self):
    #     asdasdasda
    #     sdasdasd



db = Database(SQLALCHEMY_DATABASE_URL)  #singleton
