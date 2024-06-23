from datetime import date
from res.database import db

import requests

from models.ticket import Ticket
from models.query import Query, QueryModel
from models.incident import Incident, IncidentModel

class Client_service():