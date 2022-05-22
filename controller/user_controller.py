from model.user_model import UserModel
from typing import List
from sqlalchemy.orm import Session

# Function to get list of all users
def get_all_users(session: Session, limit: int, offset: int) -> List[UserModel]:
    users_list = session.query(UserModel).offset(offset).limit(limit).all()

    return users_list
