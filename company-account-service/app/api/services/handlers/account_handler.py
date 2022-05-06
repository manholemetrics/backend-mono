from app.api.authentication.authentication import get_password_hash
from app.api.exceptions.not_found_exception import AccountNotFoundException
from app.api.models.models.account_models import Account, AccountInfo, Accounts
from app.api.services.mappers.permission_mapper import permissions_to_sqlpermissions
from app.api.sqlalchemy_models.models import SQLCompany, SQLAccount
from app.api.services.mappers.account_mapper import account_to_sqlaccount, sqlaccount_to_account_info
from app.api.sqlalchemy_models.db import session
import app.api.sqlalchemy_models.manager as db_manager 


def get_company_accounts_list(company : SQLCompany) -> Accounts:
    '''Returns an Accounts object that contains a list of accounts associated with a company'''
    accounts = Accounts.construct()
    accounts.accounts = [sqlaccount_to_account_info(account) for account in company.accounts]
    return accounts

def query_account(account_id : str, company_id : str) -> AccountInfo:
    #sqlaccount : SQLAccount = session.query(SQLAccount).filter_by(id = account_id).first()
    sqlaccount = db_manager.get_SQLAccount(account_id, company_id)
    if sqlaccount is None: raise AccountNotFoundException(sqlaccount)
    return sqlaccount_to_account_info(sqlaccount)

def create_account(new_account : Account) -> Account:
    '''Inserts an account into the database and return the account information'''
    sqlaccount = account_to_sqlaccount(new_account)
    #TODO hash password and create salt
    sqlaccount.password_hash = get_password_hash(new_account.password)
    #session.add(sqlaccount)
    #session.commit()
    db_manager.save_SQLAccount(sqlaccount)
    return sqlaccount_to_account_info(sqlaccount)

def modify_account(account : Account, existing_sqlaccount : SQLAccount):
    #ensure that modifications aren't made to important settings
    if account.permission is not None: existing_sqlaccount.permissions = permissions_to_sqlpermissions(account.permission)
    if account.password is not None: existing_sqlaccount.password_hash = get_password_hash(account.password)
    if account.email is not None: existing_sqlaccount.email = account.email
    #session.add(existing_sqlaccount)
    #session.commit()
    db_manager.save_SQLAccount(existing_sqlaccount)
    return sqlaccount_to_account_info(existing_sqlaccount)

def delete_account(sqlaccount : SQLAccount):
    '''Delete an account given an account id'''
    #session.delete(sqlaccount)
    #session.commit()
    db_manager.delete_SQLAccount(SQLAccount)
    


