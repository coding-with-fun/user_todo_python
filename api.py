from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_utils.cbv import cbv
from controller.user_controller import get_all_users
from database import get_db, db_engine, Base


Base.metadata.create_all(bind=db_engine)

router = APIRouter()

@cbv(router)
class User:
    session: Session = Depends(get_db)

    @router.get('/')
    def get_all_users_api(self, limit: int = 10, offset: int = 0):
        users_list = get_all_users(self.session, limit, offset)
        response = {
            "limit": limit,
            "offset": offset,
            "data": users_list
        }

        return response
