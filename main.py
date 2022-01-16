# from test_main import app 
import requests
from app import app
from fastapi.testclient import TestClient

client = TestClient(app)
# def test_read_root():
#     response = client.get('/')
#     assert response.status_code==200 
#     assert response.json() == {'message': 'halo world'}

data = {
    "name": "shaun",
    "due_date": "jumat",
    "description": "cantik"
}

def test_app_post():
    response = client.post("/post", json=data)
    assert response.status_code == 200
    assert data in response.json()
def test_app_get():
    response = client.get('/post', json=list(data))
    assert response.status_code==200
    assert data in response.json()


