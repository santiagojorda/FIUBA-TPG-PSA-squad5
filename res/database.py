# my_fastapi_app/database.py
from sqlalchemy import create_engine
from datetime import date
from sqlalchemy.orm import sessionmaker
from res.base import Base
from sqlalchemy.sql import func

from models.product import Product
from models.version import Version
from models.ticket import Ticket, TicketModel, QUERY_TICKET, INCIDENT_TICKET, STATUS_NEW_TICKET, STATUS_CLOSED
from models.incident_per_task import Incident_per_task
from models.severity import Severity

from models.task import TaskModel
from typing import List

from .init_data.severities import init_data_severities

from .mocks.version_products import mock_products, mock_versions
from .mocks.tickets import mock_tickets

SQLALCHEMY_DATABASE_URL = "sqlite:///sla_support.db"

class Database(): 
    def __init__(self, db_url): 
        self.engine = create_engine(db_url, echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.drop_all()
        self.create_all()

        self.__initialize_data__()
        # self.__insert_mock_data__()

    def __initialize_data__(self):
        self.__insert_severities__()

    def __insert_mock_data__(self):
        self.__insert_mock_products_and_versions__()
        self.__insert_mock_tickets__()

    def __insert_severities__(self):
        for severity_item in init_data_severities:
            severity = Severity(response_time = severity_item)
            self.session.add(severity)

        self.session.commit()
    
    def __insert_mock_products_and_versions__(self):

        for product_item in mock_products:
            self.create_product(title=product_item['title'])

        for version_item in mock_versions:
            self.create_version(
                version_code=version_item['version_code'],
                product_id=version_item['product_id'],
                release_notes=version_item['release_notes'],
            )
        

    def __insert_mock_tickets__(self):
        for ticket_item in mock_tickets:
            print(ticket_item)
            ticket = TicketModel(
                title = ticket_item['title'],
                description = ticket_item['description'],
                client_id = ticket_item['client_id'],
                version_code = ticket_item['version_code'],
                ticket_type = ticket_item['ticket_type'],
                status = ticket_item['status'],
                employee_id = ticket_item['employee_id'],
                product_id = ticket_item['product_id'],
                playback_steps = ticket_item['playback_steps'],
                severity_id = ticket_item['severity_id'],
                response = ticket_item['response'],
                closing_date = ticket_item['closing_date']
            )
            self.create_ticket(ticket)

    def get_products(self):
        return self.session.query(Product).all()
    
    def get_product_by_id(self, product_id: int):
        return self.session.query(Product).filter(Product.id == product_id).first()

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
        version = self.session.query(Version).filter(Version.product_id == product_id, Version.version_code == version_code).first() 
        return version
    
    def __get_new_ticket_id__(self):
        id = self.session.query(func.max(Ticket.id)).scalar()

        if id == None:
            return 1
        return id + 1
    
    def create_ticket(self, ticket_data: TicketModel):
        id = self.__get_new_ticket_id__()

        ticket = Ticket(
            id = id,
            title = ticket_data.title,
            description = ticket_data.description,
            client_id = ticket_data.client_id,
            version_code = ticket_data.version_code,
            status = ticket_data.status or STATUS_NEW_TICKET,
            ticket_type = ticket_data.ticket_type,
            employee_id = ticket_data.employee_id,
            product_id = ticket_data.product_id,
            opening_date =  date.today(),
            closing_date =  ticket_data.closing_date,
            duration = ticket_data.duration,
            playback_steps = ticket_data.playback_steps,
            severity_id = ticket_data.severity_id,
            response = ticket_data.response
        )
        
        self.session.add(ticket)
        self.session.commit()
        return id
    
    def get_ticket(self, ticket_id: int):
        ticket = self.session.query(Ticket).filter(Ticket.id == ticket_id).first()
        return ticket

    def get_tickets(self, product_id: int, version_code: str):
        tickets = self.session.query(Ticket).filter(Ticket.product_id == product_id, Ticket.version_code == version_code).all()
        return tickets

    def modify_ticket(self, new_ticket: TicketModel):
        ticket = self.get_ticket(new_ticket.id)  
        if not ticket:
            return False
        
        # chequear
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
        return result
    
    def get_tasks(self, ticket_id: int):
        tasks = self.session.query(Incident_per_task).filter(Incident_per_task.ticket_id == ticket_id).all()
        return tasks
    
    def delete_tasks(self, ticket_id: int):
        self.session.query(Incident_per_task).filter(
            Incident_per_task.ticket_id == ticket_id
        ).delete()

    def insert_tasks(self, ticket_id: int, tasks_data: List[TaskModel]):
        self.delete_tasks(ticket_id)

        for task in tasks_data:
            incident = Incident_per_task(
                # product_id = product_id,
                # version_code = version_code,
                ticket_id = ticket_id,
                task_id = task.task_id,
                project_id = task.project_id
            )
            res = self.session.query(Incident_per_task).filter(
                Incident_per_task.ticket_id == ticket_id,
                # Incident_per_task.version_code == version_code,
                # Incident_per_task.product_id == product_id,
                Incident_per_task.task_id == task.task_id,
                Incident_per_task.project_id == task.project_id,
            ).first()

            if not res:
                self.session.add(incident)
            else:
                return False
        
        self.session.commit()
        return True
    
    def add_and_commit(self, register):
        self.session.add(register)
        self.session.commit()

    def create_product(self, title: str):
        product = Product(title=title)
        self.add_and_commit(product)
        return product.id

    def create_version(self, product_id: int, version_code: str, release_notes: str):
        version = Version(
                version_code = version_code,
                product_id = product_id,
                release_notes = release_notes
            )
        self.add_and_commit(version)

    def drop_all(self):
        Base.metadata.drop_all(bind=self.engine)

    def create_all(self):
        Base.metadata.create_all(bind=self.engine)
db = Database(SQLALCHEMY_DATABASE_URL)
