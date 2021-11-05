from fastapi import FastAPI
# from fastapi.testclient import TestClient

app = FastAPI()

@app.get('/')
async def root_client():
    return {'message': 'halo world'}

# client = TestClient(app)
# def test_read_root():
#     response = client.get('/')
#     assert response.status_code==200 
#     assert response.json() == {'message': 'halo world'}

#didalam testing, gunakan pytest modul
#pip install pytest
#di command ketik pytest test_main.py
