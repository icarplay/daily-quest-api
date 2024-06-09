from fastapi import FastAPI
from daily_quest_api.controllers import user_routes

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Hello World'}

app.include_router(user_routes)