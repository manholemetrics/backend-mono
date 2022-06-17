import time
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.api.authentication.authentication import Permissions, Token, TokenData, authenticate_user, create_access_token
from app.api.configs.configs import environmentSettings
from app.api.main import app
from app.api.sqlalchemy_models.models import SQLAccount
import app.api.sqlalchemy_models.manager as db_manager 


@app.post('/token', response_model=Token, tags=["Token"])
async def get_token(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    '''Returns an auth token for an account login
    '''
    sqlaccount  = await db_manager.SQLAccountManger.get_SQLAccount_with_email(form_data.username)
    if not sqlaccount:
        print('error2')
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not authenticate_user(sqlaccount, form_data.password): 
        print('error')
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token_data : TokenData = TokenData.construct()
    token_data.company_id = sqlaccount.company_id
    token_data.account_id = sqlaccount.account_id
    token_data.permission = Permissions(**sqlaccount.permissions.__dict__)
    token_data.exp = time.time() + environmentSettings.jwt_exp
    access_token = create_access_token(token_data)
    return {"access_token": access_token, "token_type": "bearer"}