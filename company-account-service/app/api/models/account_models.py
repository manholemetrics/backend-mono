from typing import List, Optional
from pydantic import BaseModel

class Permissions(BaseModel):
    view_devices : bool
    register_devices : bool
    manage_devices : bool
    manage_accounts : bool
    view_device_data : bool

class AccountInfo(BaseModel):
    id : Optional[str]
    email : str
    company_id : Optional[str]
    permission : Permissions

class Account(AccountInfo):
    password : str

class Accounts(BaseModel):
    accounts : List[AccountInfo]