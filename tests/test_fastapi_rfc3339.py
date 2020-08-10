from fastapi_rfc3339 import __version__
from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
from rfc3339_validator import validate_rfc3339
from fastapi.testclient import TestClient
app = FastAPI()

class Foo(BaseModel):
    datetime1 : datetime
    datetime2 : datetime

@app.get("/", response_model=Foo)
def get_it():
    return {
        "datetime1": datetime(2020,8,10,12,12,12),
        "datetime2": datetime(2020,8,10,12,12,12,100)
    }


client = TestClient(app)
def test_rfc3339():
    response = client.get("/")
    assert response.status_code == 200
    assert validate_rfc3339(response.json()["datetime1"])
    assert validate_rfc3339(response.json()["datetime2"])
