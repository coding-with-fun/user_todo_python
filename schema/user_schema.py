from typing import List, Optional
from pydantic import BaseModel


# To support user creation
class CreateUser(BaseModel):
    firstName: str
    lastName: str

# To support user update
class UpdateUser(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]

# To support user details
class UserDetails(CreateUser):
    id: int

    class Config:
        orm_mode = True

# To support list of users
class GetUsersList(BaseModel):
    data: List[UserDetails]
