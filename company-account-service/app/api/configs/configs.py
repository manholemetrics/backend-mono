from pydantic import BaseSettings, BaseModel

class EnvironmentSettings(BaseSettings):
    secret : str = "secret"
    jwt_secret : str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    jwt_algorithm : str = "HS256"
    jwt_exp : int = 6000
    local_run : bool = False
    database_url : str = "postgresql+asyncpg://test:test@localhost:5433/"
    queue_broker_url : str = ""
    ENV : str = ""

environmentSettings = EnvironmentSettings()

class Config:
    application_name : str = "company-account-service"
    version = "0.0.1"