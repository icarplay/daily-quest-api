from daily_quest_api.services import UserService
from daily_quest_api.database import get_db
from daily_quest_api.entities import UserResponse, ResponseModel
from sqlalchemy.orm import Session
from fastapi import APIRouter
from fastapi import Depends
from typing import List

user_routes = APIRouter()
user_service = UserService()

@user_routes.get('/users/', response_model=ResponseModel[List[UserResponse]])
def get_users(db: Session = Depends(get_db)):
    return user_service.get_all(db)

@user_routes.get('/users/{id}', response_model=ResponseModel[UserResponse])
def get_user_by_id(id: str, db: Session = Depends(get_db)):
    return user_service.get_by_id(id, db)

@user_routes.post('/users', response_model=ResponseModel[UserResponse])
def create_user(name: str, email: str, password: str, db: Session = Depends(get_db)):
    return user_service.create(name, email, password, db)