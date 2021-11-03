from fastapi import FastAPI, HTTPException, Form
from typing import List
from models import Package, PackageIn, Todo

app = FastAPI()

#tutorial3
@app.post('/bahasa')
async def bahasa_post(name:str=Form(...), type:str=Form(...)):
    return {
        'name':name,
        'type': type
    }

#tutorial2
store_database = []

@app.get('/get')
async def getting():
    return {
        'salute' : 'haiii...'
    }

@app.post('/post/')
async def posting(todo:Todo):
    store_database.append(todo)
    return store_database

@app.get('/todo', response_model=List[Todo])
async def get_all_todo():
    return store_database

@app.get('/put/{id}')
async def put_data(id:int):
    try:
        return store_database[id]
    except:
        raise HTTPException(status_code=404, detail='Todo Not Found')

@app.put('/get/{id}')
async def update_todo(id:int, todo:Todo):
    try:
        store_database[id] = todo
        return store_database[id]
    except:
        raise HTTPException(status_code=404, detail='Todo Not Found')

@app.delete('/delete/{id}')
async def deleta_data(id:int):
    try:
        obj = store_database[id]
        store_database.pop(id)
        return obj 
    except:
        raise HTTPException(status_code=404, detail='Todo Not Found')


#tutorial1
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

