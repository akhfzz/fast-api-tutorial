from fastapi import FastAPI
from models import Package, PackageIn

app = FastAPI()

# uvicorn name_file:name_root_lib --reload
@app.get('/')
async def say_to_world():
    return {
        'sender': 'hallo world!'
    }

@app.get('/component/{component_id}')
async def get_component(component_id:int):
    return {
        'Komponen' : component_id,
    }

@app.get('/component')
async def read_component(number:int, text:str):
    return {
        'number': number,
        'text' : text
    }

@app.post('/package/{priority}')
async def make_package(priority:int,package:Package, value:bool):
    return {
        'priority': priority,
        **package.dict(),
        'value': value
    }

#exclude mengecualikan suatu atribut sedangkan include hanya menyisipkan atribut tertentu
@app.post('/package2/', response_model=Package, response_model_include={'name'})
async def post_package(package:PackageIn):
    return package