from fastapi import FastAPI
from app.api.configs.configs import Config, environmentSettings
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(    
    title=Config.application_name
)

origins = [
    "https://dashboard-deploy-h3gpr.ondigitalocean.app/"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.api.routes.account_routes import *
from app.api.routes.authentication_routes import *
if environmentSettings.ENV == "DEV": 
    from app.api.routes.test_routes import *

# broker = Broker(brokerConfig.url)
# broker.create_all()
# broker.run()

# @app.on_event("shutdown")
# def shutdown_event():
#     session.close()
