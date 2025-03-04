import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    id: int
    name : str
    email: EmailStr
    password: str
    created_at: datetime  = datetime.now()
    
    
class File(BaseModel):
    class File(BaseModel):
        id: int
        file_name: str
        file_type: str
        file_size: int
        file_path: str  
        date_created: datetime = datetime.now()
        date_modified: datetime = datetime.now()
        owner_id: int 
        folder_id: int 
        version: int = 1 
        shared_with: list[int] = [] 

class Folder(BaseModel):
    
    id: int
    folder_name: str
    date_created: datetime = datetime.now()
