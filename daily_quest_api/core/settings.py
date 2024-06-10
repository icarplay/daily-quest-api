from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    env: str
    db_user: str
    db_password: str
    db_host: str
    db_name: str
    secret_key: str

    class Config:
        env_file = ".env"