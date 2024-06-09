from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config
import os

DB_USER = config('USER') if os.environ.get('USER') is None else os.environ.get('USER')
DB_PASSWORD = config('PASSWORD') if os.environ.get('PASSWORD') is None else os.environ.get('PASSWORD')
DB_HOST = config('HOST') if os.environ.get('HOST') is None else os.environ.get('HOST')
SECRET_KEY = config('SECRET_KEY') if os.environ.get('SECRET_KEY') is None else os.environ.get('SECRET_KEY')
DB_NAME = config('DB_NAME') if os.environ.get('DB_NAME') is None else os.environ.get('DB_NAME')

host: str = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?retryWrites=true&w=majority"

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    host, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class DbContextManager:
    def __init__(self):
        self.db = SessionLocal()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


async def get_db():
    with DbContextManager() as db:
        yield db