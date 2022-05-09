import time
from typing import Optional

from fastapi.params import Depends
from app.api.configs.configs import environmentSettings
from app.api.exceptions.authentication_exception import InvalidAccessToken

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
    #print("auth")
    try:
     #   print(token)
        payload = jwt.decode(token, environmentSettings.jwt_secret, algorithms=[environmentSettings.jwt_algorithm])
      #  print(payload)
        tokenData = TokenData(**payload)
       # print(tokenData)
        if tokenData.exp < int(time.time()): raise InvalidAccessToken(token, "expired")
        return tokenData
    except:
       # print("fail")
        pass
    raise InvalidAccessToken(token, "find token")