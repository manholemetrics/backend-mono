import queue
from celery import Celery
from app.api.configs.configs import environmentSettings, config
celery = Celery(config.application_name, broker=environmentSettings.broker)
from pydantic import BaseModel
from fastapi import FastAPI

celery.conf.update(
    {
    'task_routes': {
        'fetch_data': {'queue': 'fetch_data'},
    }
    }
)

class Schema(BaseModel):
    name : str
    age : int


@celery.task(exchange = "fetch_data")
def fetch_data(message):
    print("message")

schema = Schema.construct()
schema.name = "max"
schema.age = 14
#create_order(schema)
celery.send_task('fetch_data', kwargs={'message': schema.dict()})
celery.send_task('fetch_data', kwargs={'url': schema.dict()})

# Create FastAPI app
app = FastAPI()