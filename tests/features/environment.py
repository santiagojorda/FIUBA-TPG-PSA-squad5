from fastapi.testclient import TestClient
from res.database import db
from main import app

def before_all(context):
    context.client = TestClient(app)


def before_scenario(context, scenario):
    db.create_all()

def after_scenario(context, scenario):
    db.drop_all()
