from fastapi.params import Depends
from app.api.authentication.authentication import TokenData, token_authentication
from app.api.exceptions.authentication_exception import InvalidPermissionException
from app.api.main import app
from app.api.models.account_models import AccountInfo, Accounts, Account
from fastapi import Body
from app.api.services.account_handler import AccountHandler
from app.api.services.company_handler import CompanyHandler
 
# working
@app.get('/accounts/accounts', response_model=Accounts, tags=["Account"])
async def get_accounts(token_data : TokenData = Depends(token_authentication)) -> Accounts:
    '''Get the list of accounts associated with a company, requires manage_accounts permission'''
    if token_data.permission.manage_accounts != True : raise InvalidPermissionException(token_data,"")
    company_handler = await CompanyHandler.create(token_data.company_id)
    return company_handler.get_company_accounts_list()

# working
@app.get('/accounts/account/{account_id}', response_model=AccountInfo, tags=["Account"])
async def get_account(account_id : str, token_data : TokenData = Depends(token_authentication)) -> AccountInfo:
    if token_data.permission.manage_accounts != True : raise InvalidPermissionException(token_data,"")
    account_handler = await AccountHandler.create(account_id, token_data.company_id)
    account_info = account_handler.get_account_info()
    return account_info

# working
@app.post('/accounts/account', response_model=AccountInfo, tags=["Account"])
async def post_account(new_account : Account = Body(...), token_data : TokenData = Depends(token_authentication)) -> AccountInfo:
    if token_data.permission.manage_accounts != True: raise InvalidPermissionException(token_data,"")
    account_info = await AccountHandler.create_account(new_account, token_data.company_id)
    return account_info

# not working
@app.put('/accounts/account', response_model=AccountInfo, tags=["Account"])
async def put_account(account : AccountInfo = Body(...), token_data : TokenData = Depends(token_authentication)) -> AccountInfo:
    if token_data.permission.manage_accounts != True : raise InvalidPermissionException(token_data,"Not able to modify accounts")
    account_handler = await AccountHandler.create(account.id, token_data.company_id)
    account_info = await account_handler.modify(account)
    return account_info

# working
@app.delete('/accounts/account/{account_id}', tags=["Account"])
async def delete_account(account_id : str, token_data : TokenData = Depends(token_authentication)):
    '''Delete an account, requires manage_accounts permission'''
    if token_data.permission.manage_accounts != True : raise InvalidPermissionException(token_data,"")
    account_handler = await AccountHandler.create(account_id, token_data.company_id)
    await account_handler.delete()
    print('deleted')
    return

