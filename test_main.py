from behave.__main__ import main as behave_main
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

behave_main("tests/features")

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200