from fastapi import FastAPI
from app.api.configs.configs import Config, environmentSettings
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(    
    title=Config.application_name
)

# origins = [
#     "https://dashboard-deploy-h3gpr.ondigitalocean.app/"
# ]


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


from app.api.sqlalchemy_models.db import engine
from app.api.sqlalchemy_models.models import Base

@app.on_event("startup")
async def startup():
    if environmentSettings.ENV == 'DEV':
        print('setup')
        try:
            async with engine.begin() as conn:
                # await conn.run_sync(Base.metadata.drop_all)
                await conn.run_sync(Base.metadata.create_all)
        except:
            ...