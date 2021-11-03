from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class PackageIn(BaseModel):
    secret_id: int
    name: str
    number: str 
    description: Optional[str] =None

class Package(BaseModel):
    name: str
    number: str 
    description: Optional[str] =None

class Todo(BaseModel):
    name: str
    due_date: str
    description: str 

class Mahasiswa(models.Model):
    id = fields.IntField(pk=True)
    nama = fields.CharField(max_length=250)
    nim = fields.IntField()

    class PydanticMeta:
        pass 

mahasiswa_pydantic = pydantic_model_creator(Mahasiswa, name='mhs')
mahasiswaIn_pydantic = pydantic_model_creator(Mahasiswa, name='mhsIn', exclude_readonly=True)

class RegisterIn(BaseModel):
    name:str=Field(...)

class Register(BaseModel):
    id: int
    name: str 
    date_posted: datetime