from pydantic import BaseSettings, BaseModel

class EnvironmentSettings(BaseSettings):
    secret : str = "secret"
    jwt_secret : str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    jwt_algorithm : str = "HS256"
    local_run : bool = False
    mongo_database_url : str = 'mongodb://localhost:27017/'#"mongodb+srv://doadmin:sv1T8067gx2pq5Y9@company-device-service-690ea96d.mongo.ondigitalocean.com/admin?authSource=admin&replicaSet=company-device-service&tls=true&tlsCAFile=ca-certificate.crt"
    queue_broker_url : str = ""
    ENV : str = ""

environmentSettings = EnvironmentSettings()
print(environmentSettings.database_url)
class Config:
    application_name : str = "company-device-service"
    version : str = "0.0.1"