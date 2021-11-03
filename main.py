from fastapi import FastAPI, HTTPException, Form
from typing import List
from models import Mahasiswa, mahasiswa_pydantic, mahasiswaIn_pydantic
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise 
from fastapi.middleware.cors import CORSMiddleware
#mahasiswaIn_pydantic sebagai inputan yakni menampilkan form sesuai dengan models
#mahasiswa_pydantic sebagai output pada response model

app = FastAPI()

@app.post('/input', response_model=mahasiswa_pydantic)
async def create(input: mahasiswaIn_pydantic):
    obj = await Mahasiswa.create(**input.dict(exclude_unset=True))#model membuat data
    return await mahasiswa_pydantic.from_tortoise_orm(obj) #response model membuat orm

@app.get('/get/{id}', response_model=mahasiswa_pydantic, responses={404: {'model': HTTPNotFoundError}})
async def get_data(id:int):
    return await mahasiswa_pydantic.from_queryset_single(Mahasiswa.get(id=id))

@app.put('/update/{id}', response_model=mahasiswa_pydantic, responses={404: {'model':HTTPNotFoundError}})
async def put_data(id:int, mhs:mahasiswaIn_pydantic):
    await Mahasiswa.filter(id=id).update(**mhs.dict(exclude_unset=True))
    return await mahasiswa_pydantic.from_queryset_single(Mahasiswa.get(id=id))

@app.delete('/delete/{id}', responses={404:{'model':HTTPNotFoundError}})
async def delete_data(id:int):
    delete_obj = await Mahasiswa.filter(id=id).delete()
    if not delete_obj:
        raise HTTPException(status_code=404, detail='data is not found')
    return {'success': 'Ok you have delete once data'}


#otomatis create table pada database
register_tortoise(
    app,
    db_url='mysql://root:@localhost/testing', #testing adalah nama database
    modules={'models':['models']},
    generate_schemas=True,
    add_exception_handlers=True
)
origins = [
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)