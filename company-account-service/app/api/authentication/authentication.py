import time
from typing import Optional

from fastapi.params import Depends
from app.api.configs.configs import environmentSettings
from app.api.exceptions.authentication_exception import InvalidAccessToken

from app.api.sqlalchemy_models.models import SQLAccount, SQLCompany

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class Permissions(BaseModel):
    view_devices : Optional[bool] = False
    register_devices : Optional[bool] = False
    manage_devices : Optional[bool] = False
    manage_accounts : Optional[bool] = False
    view_device_data : Optional[bool] = False

class TokenData(BaseModel):
    company_id: str 
    account_id: str
    permission: Permissions
    exp : int

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def token_authentication(token: str = Depends(oauth2_scheme)) -> TokenData:
    try:
        payload = jwt.decode(token, environmentSettings.jwt_secret, algorithms=[environmentSettings.jwt_algorithm])
        tokenData = TokenData(**payload)
        if tokenData.exp < int(time.time()): raise InvalidAccessToken(token, "expired")
        return tokenData
    except:
        pass
    raise InvalidAccessToken(token, "find token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(sqlaccount : SQLAccount, password : str):    
    return verify_password(password, sqlaccount.password_hash)

def create_access_token(data: TokenData):
    to_encode = data.dict()
    encoded_jwt = jwt.encode(to_encode, environmentSettings.jwt_secret, algorithm=environmentSettings.jwt_algorithm)
    return encoded_jwt