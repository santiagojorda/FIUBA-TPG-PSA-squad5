from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.product import Product
from models.ticket import Ticket
from models.version import Version
from models.task import Task
from models.proyect import Proyect

Base = declarative_base()
TABLE_NAME = "tbl_incidente_por_tarea"

TASK_ID_COLUMN_NAME = "task_id"
PROYECT_ID_COLUMN_NAME = "proyect_id"
TICKET_ID_COLUMN_NAME = "ticket_id"
VERSION_ID_COLUMN_NAME = "verion_id"
PRODUCT_ID_COLUMN_NAME = "product_id"

class Incidente_por_tarea(Base):
    __tablename__ = TABLE_NAME
    ID_incidente_por_tarea = Column(Integer, primary_key=True, autoincrement=True)
    
    ID_task = Column(TASK_ID_COLUMN_NAME, Integer)
    ID_proyect = Column(PROYECT_ID_COLUMN_NAME, Integer)
    ID_ticket = Column(TICKET_ID_COLUMN_NAME, Integer, ForeignKey(Ticket.getIDColumnName()))
    ID_version = Column(VERSION_ID_COLUMN_NAME, Integer, ForeignKey(Version.getIDColumnName()))
    Id_product = Column(PRODUCT_ID_COLUMN_NAME, Integer, ForeignKey(Product.getIDColumnName()))    

    def __str__(self):
        return f"id_task: {self.ID_TASK}, id_ticket: {self.ID_ticket}, id_version: {self.ID_version}, id_proyect: {self.ID_proyect}, id_product: {self.Id_product}"


# sqlalchemy.Column(
#                 "product_id", sqlalchemy.ForeignKey("product_table.product_id", ondelete = "CASCADE")
#             ),
# sqlalchemy.Column(
#                 "version_id", sqlalchemy.ForeignKey("version_table.version_id", ondelete = "CASCADE")
#             ),
# sqlalchemy.Column(
#                 "ticket_id", sqlalchemy.ForeignKey("ticket_table.ticket_id", ondelete = "CASCADE")
#             ),
# sqlalchemy.Column(
#                 "project_id", sqlalchemy.ForeignKey("project_table.project_id", ondelete = "CASCADE")
#             ),
# sqlalchemy.Column(
#                 "task_id", sqlalchemy.ForeignKey("task_table.task_id", ondelete = "CASCADE")
#             ),

# sqlalchemy.PrimaryKeyConstraint("task_id", "project_id", "product_id", "version_id", "ticket_id")