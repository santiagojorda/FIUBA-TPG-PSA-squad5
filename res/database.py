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
        self.__insert_tickets__()

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
        siu_version1 = Version(version_code="1.1.0", product_id = 0, release_notes='Email comunication')
        self.session.add(siu_version1)
        siu_version2 = Version(version_code="2.2.0", product_id = 0, release_notes='Exam notes app')
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

    def __insert_tickets__(self):
        product1 = self.get_version_by_product_id(0, "1.1.0")
        incident_siu = TicketModel(
            title = "Email Application Crashing",
            description = "Email Application crash when attempting to access",
            client_id = 0,
            version_code = product1.version_code,
            status = STATUS_NEW_TICKET,
            ticket_type = INCIDENT_TICKET,
            employee_id = 1,
            product_id = product1.product_id,
            playback_steps = """Open the email application by clicking on the application icon on the desktop or from the start menu.
                Observe that the application begins to load but crashes within a few seconds.""",
            severity_id = 2
        )

        query_siu = TicketModel(
            title = "Profile Image",
            description = "Im wondering to change image of my profile",
            client_id = 0,
            version_code = product1.version_code,
            status = STATUS_CLOSED,
            ticket_type = QUERY_TICKET,
            employee_id = 1,
            closing_date= date.today(),
            product_id = product1.product_id,
            response = """Once logged in, locate your profile icon or name, usually found at the top right corner of the page.
                Click on your profile icon or name to open a dropdown menu.
                Select "Settings" or "Profile" from the dropdown menu.
            """
        )

        
        self.create_ticket(incident_siu)
        self.create_ticket(query_siu)
        query_siu.closing_date = date.today()
        query_siu.status = STATUS_CLOSED
        query_siu.id = 2
        self.modify_ticket(query_siu)

        product2 = self.get_version_by_product_id(0, "2.2.0")

        query_siu2 = TicketModel(
            title = "Request for Professor's Email Address",
            description = "Im wondering to get the email of professor to send a message",
            client_id = 0,
            version_code = product2.version_code,
            ticket_type = QUERY_TICKET,
            employee_id = 1,
            product_id = product2.product_id,
            response = """Navigate to the "Faculty" or "Staff Directory" section.
                Use the search function to find the professor by name or department.
                The directory listing usually includes contact details such as email addresses.
            """
        )

        
        self.create_ticket(query_siu2)

        query_siu2.closing_date = date.today()
        query_siu2.status = STATUS_CLOSED
        query_siu2.id = 3
        self.modify_ticket(query_siu2)


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
        version = self.session.query(Version).filter(Version.product_id == product_id, Version.version_code == version_code).first() 
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
            version_code = ticket_data.version_code,
            status = 0,
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
        self.session.query(Incident_per_task).filter(
            Incident_per_task.product_id == product_id,
            Incident_per_task.version_code == version_code,
            Incident_per_task.ticket_id == ticket_id
        ).delete()


        for task in tasks_data:
            incident = Incident_per_task(
                product_id = product_id,
                version_code = version_code,
                ticket_id = ticket_id,
                task_id = task.task_id,
                project_id = task.project_id
            )
            res = self.session.query(Incident_per_task).filter(
                Incident_per_task.ticket_id == ticket_id,
                Incident_per_task.version_code == version_code,
                Incident_per_task.product_id == product_id,
                Incident_per_task.task_id == task.task_id,
                Incident_per_task.project_id == task.project_id,
            ).first()

            if not res:
                self.session.add(incident)
            else:
                return False
        
        self.session.commit()
        return True

db = Database(SQLALCHEMY_DATABASE_URL)
