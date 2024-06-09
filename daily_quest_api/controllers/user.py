from daily_quest_api.services import UserService
from daily_quest_api.database import get_db
from daily_quest_api.entities import User
from sqlalchemy.orm import Session
from fastapi import APIRouter
from fastapi import Depends

# from core.settings import Settings

# settings = Settings()
# exemplo de uso settings:  
# str(settings.model_dump()['env'])

user_routes = APIRouter()
user_service = UserService()

@user_routes.get('/users/{id}', response_model=User, response_model_by_alias=False)
def get_user_by_id(id: str, db: Session = Depends(get_db)):
    return user_service.get_by_id(id, db)

@user_routes.post('/users', response_model=User, response_model_by_alias=False)
def create_user(name: str, email: str, password: str, db: Session = Depends(get_db)):
    return user_service.create(name, email, password, db)