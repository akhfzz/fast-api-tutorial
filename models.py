from pydantic import BaseModel
from typing import Optional

class PackageIn(BaseModel):
    secret_id: int
    name: str
    number: str 
    description: Optional[str] =None

class Package(BaseModel):
    name: str
    number: str 
    description: Optional[str] =None