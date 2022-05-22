from sqlalchemy import Column, Integer, String, true
from database import Base

class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String(20))
    lastName = Column(String(20))
