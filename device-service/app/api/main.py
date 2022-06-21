from re import L
from fastapi import FastAPI
from app.api.configs.configs import Config, environmentSettings
from starlette.middleware.cors import CORSMiddleware
from beanie import init_beanie
from schemas.device_mongo_models.device_models import MongoDevice
import motor
import os
from celery import Celery

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


app = FastAPI(
    title=Config.application_name, 
    #version=Config.version
)

from app.api.routes.device_routes import *
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


@app.on_event("startup")
async def app_init():
   client = motor.motor_asyncio.AsyncIOMotorClient(environmentSettings.mongo_database_url)
   await init_beanie(database=client.db_name, document_models=[MongoDevice])
