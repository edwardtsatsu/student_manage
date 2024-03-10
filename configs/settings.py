from pydantic_settings import BaseSettings


# Validate the environment variable before the  booting the app
class Settings(BaseSettings):
    database_password: str
    database_username: str
    database_name: str
    database_port: str
    database_host: str
    jwt_secret_key: str
    secret_key: str

    class Config:
        env_file = ".env"


settings = Settings()