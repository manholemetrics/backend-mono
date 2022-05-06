from re import L
from fastapi import FastAPI
from app.api.configs.configs import Config, environmentSettings
from mongoengine import connect
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title=Config.application_name, 
    #version=Config.version
)

from app.api.routes.device_routes import *
from app.api.routes.device_registration_routes import *
if environmentSettings.ENV == "DEV":
    from app.api.routes.test_routes import *

origins = [
    "http://localhost",
    "https://dashboard-deploy-h3gpr.ondigitalocean.app",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


connect(host = environmentSettings.database_url)

# broker = Broker(brokerConfig.url)
# broker.create_all()
# broker.run()