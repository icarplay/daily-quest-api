from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    env: str
    app_name: str

    class Config:
        env_file = ".env"