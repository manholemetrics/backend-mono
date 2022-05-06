from fastapi.params import Depends
from starlette.requests import Request
from app.api.authentication.authentication import TokenData, token_authentication
from app.api.exceptions.authentication_exception import InvalidPermissionException
from app.api.exceptions.not_found_exception import CompanyNotFoundException
from app.api.main import app
import app.api.services.handlers.account_handler as account_handler
from app.api.models.models.account_models import AccountInfo, Accounts, Account
from fastapi import Body
from app.api.sqlalchemy_models.db import session
from app.api.sqlalchemy_models.models import SQLAccount, SQLCompany
import app.api.sqlalchemy_models.manager as db_manager 
 
@app.get('/accounts/accounts', response_model=Accounts, tags=["Account"])
async def get_accounts(tokenData : TokenData = Depends(token_authentication)) -> Accounts:
    '''Get the list of accounts associated with a company, requires manage_accounts permission'''
    if tokenData.permission.manage_accounts != True : raise InvalidPermissionException(tokenData,"")
    #company = session.query(SQLCompany).filter_by(id = tokenData.company_id).first()
    company = db_manager.get_SQLCompany(tokenData.company_id)
    if company is None: return CompanyNotFoundException(tokenData.company_id)
    return account_handler.get_company_accounts_list(company)

@app.get('/accounts/account/{account_id}', response_model=AccountInfo, tags=["Account"])
async def get_account(account_id : str, tokenData : TokenData = Depends(token_authentication)) -> Account:
    '''Get account information'''
    if tokenData.permission.manage_accounts != True : raise InvalidPermissionException(tokenData,"")
    account = account_handler.query_account(account_id, tokenData.company_id)
    #if str(account.company_id) != str(tokenData.company_id):  raise InvalidPermissionException(tokenData,"")
    return account

@app.post('/accounts/account', response_model=AccountInfo, tags=["Account"])
async def post_account(new_account : Account = Body(...), tokenData : TokenData = Depends(token_authentication)) -> AccountInfo:
    '''Create an account, requires an account email and an account password, requires manage_accounts permission'''
    if tokenData.permission.manage_accounts != True: raise InvalidPermissionException(tokenData,"")
    #sqlaccount : SQLAccount = session.query(SQLAccount).filter_by(email = new_account.email).first()
    sqlaccount = db_manager.get_SQLAccount_with_email(new_account.email)
    if sqlaccount is not None: raise InvalidPermissionException(tokenData,"email taken")
    company_id = tokenData.company_id
    new_account.company_id = company_id
    account = account_handler.create_account(new_account)
    return account

@app.put('/accounts/account', response_model=AccountInfo, tags=["Account"])
async def put_account(account : Account = Body(...), tokenData : TokenData = Depends(token_authentication)) -> AccountInfo:
    '''Modify an account, allows changing of account password, account permissions and account email, requires manage_accounts permission'''
    if tokenData.permission.manage_accounts != True : raise InvalidPermissionException(tokenData,"Not able to modify accounts")
    #sqlaccount : SQLAccount = session.query(SQLAccount).filter_by(id = account.id, company_id = int(tokenData.company_id)).first()
    sqlaccount = db_manager.get_SQLAccount(account.id, tokenData.company_id)
    if sqlaccount is None: raise InvalidPermissionException(tokenData,"Account not found")
    # check if email is new and it is already taken
    if account.email is not None and account.email != sqlaccount.email:
        check_email_account : SQLAccount = session.query(SQLAccount).filter_by(email = account.email).first()
        if check_email_account is not None: raise InvalidPermissionException(tokenData,"email taken")
    modified_account = account_handler.modify_account(account,sqlaccount)
    return modified_account

@app.delete('/accounts/account/{account_id}', tags=["Account"])
async def delete_account(account_id : str, tokenData : TokenData = Depends(token_authentication)):
    '''Delete an account, requires manage_accounts permission'''
    if tokenData.permission.manage_accounts != True : raise InvalidPermissionException(tokenData,"")
    company_id = tokenData.company_id
    #sqlaccount = session.query(SQLAccount).filter_by(id = int(account_id), company_id = int(company_id)).first()
    sqlaccount = db_manager.get_SQLAccount(account.id, tokenData.company_id)
    if sqlaccount is None: raise InvalidPermissionException(tokenData,"")
    print(tokenData.company_id)
    account_handler.delete_account(sqlaccount)
    return

#TODO change password


