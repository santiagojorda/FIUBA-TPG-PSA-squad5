# my_fastapi_app/database.py
from sqlalchemy import create_engine
from datetime import date
from sqlalchemy.orm import sessionmaker
from res.base import Base
from sqlalchemy.sql import func


from models.product import Product
from models.version import Version
from models.ticket import Ticket, TicketModel
from models.incident_per_task import Incident_per_task
from models.severity import Severity

from models.task import TaskModel
from typing import List

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
    
    def get_products(self):
        return self.session.query(Product).all()

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
    
    def create_ticket(self, ticket_data: TicketModel):
        id = self.session.query(func.max(Ticket.id)).scalar()
        print('el id es: ', id)

        if id == None:
            id = 1
        else: 
            id = id + 1
        print('el nuevo id es: ', id)

        ticket = Ticket(
            id = id,
            title = ticket_data.title,
            description = ticket_data.description,
            client_id = ticket_data.client_id,
            version_code= ticket_data.version_code,
            status = 0,
            ticket_type = ticket_data.ticket_type,
            employee_id = ticket_data.employee_id,
            product_id = ticket_data.product_id,
            opening_date =  date.today(),
            duration = ticket_data.duration,
            playback_steps = ticket_data.playback_steps,
            severity_id = ticket_data.severity_id,
        )
        
        self.session.add(ticket)
        self.session.commit()
        return id
    
    def get_ticket(self, ticket_id: int):
        ticket = self.session.query(Ticket).filter(Ticket.id == ticket_id).first()
        return ticket

    def get_tickets(self, product_id: int, version_code: str):
        tickets = self.session.query(Ticket).filter(Ticket.product_id == product_id, Ticket.version_code == version_code).all()
        # no devuelve cliente ni severidad, solo id de los mismos
        return tickets

    def modify_ticket(self, new_ticket: TicketModel):
        ticket = self.session.query(Ticket).filter(Ticket.id == new_ticket.id).first()
        if not ticket:
            return False
        
        ticket_dict = new_ticket.dict(exclude_unset=True)

        for key, value in ticket_dict.items():
            if value is not None:
                setattr(ticket, key, value)
        
        self.session.commit()
        self.session.refresh(ticket)
        return ticket
        
    def delete_ticket(self, ticket_id: int):
        result = self.session.query(Ticket).filter(Ticket.id == ticket_id).delete()

        self.session.commit()
        # no devuelve cliente ni severidad, solo id de los mismos
        return result
    
    def get_tasks(self, ticket_id: int):
        tasks = self.session.query(Incident_per_task).filter(Incident_per_task.ticket_id == ticket_id).all()
        return tasks
    
    def insert_tasks(self, product_id: int, version_code: int, ticket_id: int, tasks_data: List[TaskModel]):
        for task in tasks_data:
            incident = Incident_per_task(
                product_id = product_id,
                version_code = version_code,
                ticket_id = ticket_id,
                task_id = task.task_id,
                project_id = task.project_id
            )
            self.session.add(incident)
        
        self.session.commit()
        return True

db = Database(SQLALCHEMY_DATABASE_URL)  #singleton
