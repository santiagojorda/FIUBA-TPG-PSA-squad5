from sqlalchemy import Column, Integer, String, ForeignKey

from res.base import Base

from models.product import Product
from models.ticket import Ticket
from models.version import Version

TABLE_NAME = "tbl_incident_per_task"

TASK_ID_COLUMN_NAME = "task_id"
PROYECT_ID_COLUMN_NAME = "proyect_id"
TICKET_ID_COLUMN_NAME = "ticket_id"
VERSION_ID_COLUMN_NAME = "verion_id"
PRODUCT_ID_COLUMN_NAME = "product_id"

class Incident_per_task(Base):
    __tablename__ = TABLE_NAME
    ID_incidente_por_tarea = Column(Integer, primary_key=True, autoincrement=True)
    
    ID_task = Column(Integer, name=TASK_ID_COLUMN_NAME)
    ID_proyect = Column(Integer, name=PROYECT_ID_COLUMN_NAME)
    ID_ticket = Column(Integer, ForeignKey(Ticket.getIDColumnName()), name=TICKET_ID_COLUMN_NAME)
    ID_version = Column(Integer, ForeignKey(Version.getVersionCodeColumnName()), name=VERSION_ID_COLUMN_NAME)
    Id_product = Column(Integer, ForeignKey(Product.getIDColumnName()), name=PRODUCT_ID_COLUMN_NAME)    

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