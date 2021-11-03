from fastapi import FastAPI, Request
from fastapi.params import Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlalchemy 
from datetime import *
from typing import List
import databases
from models import RegisterIn, Register

app = FastAPI()
db_url = 'mysql://root:@localhost/testing' #testing adalah nama database

metadata = sqlalchemy.MetaData()

db = databases.Database(db_url)

register = sqlalchemy.Table(
    'register', #nama tabel yang akan dibuat dalam db
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(255)),
    sqlalchemy.Column('date_posted', sqlalchemy.DateTime())
)

engine = sqlalchemy.create_engine(db_url)

metadata.create_all(engine)

@app.on_event('startup')
async def connect():
    await db.connect()

@app.on_event('shutdown')
async def shutdown():
    await db.disconnect()

#contoh untuk templates
# variabel templates untuk menentukan folder mana yang akan digunakan penyimpanan file html
templates = Jinja2Templates(directory='templates')
@app.get('/user/{id}', response_class=HTMLResponse)
async def get_with_templates(request:Request, id:int):
    return templates.TemplateResponse('index.html', {"request": request, 'id':id})

#crud dalam database menggunakan sqlalchemy
@app.post('/register/', response_model=Register)
async def create(r:RegisterIn=Depends()):
    query = register.insert().values(
        name= r.name,
        date_posted= datetime.now()
    )
    record = await db.execute(query)
    query = register.select().where(register.c.id == record)
    row = await db.fetch_one(query)
    return {**row}

@app.get('/get/{id}', response_model=Register)
async def get_from_db(id:int):
    query = register.select().where(register.c.id==id)
    user = await db.fetch_one(query)
    return {**user}

@app.get('/get', response_model=List[Register])
async def get_all_from_db():
    query = register.select()
    user = await db.fetch_all(query)
    return user

@app.put('/update/{id}', response_model=Register)
async def update_data(id:int, r:RegisterIn=Depends()):
    query = register.update().where(register.c.id==id).values(
        name=r.name,
        date_posted=datetime.now()
    )
    ex = await db.execute(query)
    query = register.select().where(register.c.id==ex)
    row_line = await db.fetch_one(query)
    return {**row_line}

@app.delete('/delete/{id}', response_model=Register)
async def delete_data(id:int):
    query = register.delete().where(register.c.id==id)
    await db.execute(query)
    return {'ok': 'success'}

