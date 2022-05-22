from typing import List, Optional
from pydantic import BaseModel


# To support user creation
class User(BaseModel):
    id: int
    firstName: str
    lastName: str

    class Config:
        orm_mode = True
