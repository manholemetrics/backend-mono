from pydantic import BaseSettings, BaseModel

class EnvironmentSettings(BaseSettings):
    secret : str = "secret"
    broker : str = 'amqp://guest:guest@localhost:5672//'

environmentSettings = EnvironmentSettings()

class Config(BaseModel):
    application_name : str = "device-service"

config = Config()
