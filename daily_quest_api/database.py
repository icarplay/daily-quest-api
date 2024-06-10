from daily_quest_api.core.settings import Settings
from pymongo import MongoClient

settings = Settings()

host: str = f"mongodb+srv://{settings.db_user}:{settings.db_password}@{settings.db_host}/{settings.db_name}?retryWrites=true&w=majority"

class DbContextManager:
    def __init__(self):
        self.connection = MongoClient(host=host)
        self.db = self.connection.daily_quest

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()


async def get_db():
    with DbContextManager() as db:
        yield db