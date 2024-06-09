from daily_quest_api.services import UserService
from daily_quest_api.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter
from fastapi import Depends

# from core.settings import Settings

# settings = Settings()
# exemplo de uso settings:  
# str(settings.model_dump()['env'])

user_routes = APIRouter()
user_service = UserService()

@user_routes.get('/users/{id}')
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return { 'user': user_service.get_by_id(id, db) }

@user_routes.post('/users')
def create_user(name: str, email: str, password: str, db: Session = Depends(get_db)):
    return user_service.create(name, email, password, db)