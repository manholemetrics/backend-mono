import time
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.api.authentication.authentication import Permissions, Token, TokenData, authenticate_user, create_access_token
from app.api.configs.configs import environmentSettings
from app.api.main import app
from app.api.sqlalchemy_models.db import session
from app.api.sqlalchemy_models.models import SQLAccount
import app.api.sqlalchemy_models.manager as db_manager 


@app.post('/token', response_model=Token, tags=["Token"])
async def get_token(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    '''Returns an auth token for an account login
    '''
    # sqlaccount : SQLAccount = session.query(SQLAccount).filter_by(email = form_data.username).first()
    sqlaccount  = db_manager.get_SQLAccount_with_email(email)
    if not sqlaccount:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not authenticate_user(sqlaccount, form_data.password): 
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token_data : TokenData = TokenData.construct()
    token_data.company_id = "1"#sqlaccount.company.id
    token_data.account_id = "1"#sqlaccount.id
    token_data.permission = Permissions(**{
        "view_devices":True,
        "register_devices":True,
        "manage_devices":True,
        "manage_accounts":True,
        "view_device_data":True
    })#Permissions(**sqlaccount.permissions.__dict__)
    token_data.exp = time.time() + 10000000000#environmentSettings.jwt_exp
    access_token = create_access_token(token_data)
    print(access_token)
    return {"access_token": access_token, "token_type": "bearer"}