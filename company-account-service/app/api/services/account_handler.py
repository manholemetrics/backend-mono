from app.api.models.account_models import AccountInfo, Account
from app.api.sqlalchemy_models.models import SQLAccount
from app.api.authentication.authentication import get_password_hash
from app.api.services.mappers.account_mapper import sqlaccount_to_account_info, account_to_sqlaccount
from app.api.sqlalchemy_models.manager import SQLAccountManger 

class AccountHandler:

    _sql_account : SQLAccount
    
    async def __init__(self, account_id : int, company_id : int):
        self._sql_account = await SQLAccountManger.SQLAccountManger.get_SQLAccount(account_id, company_id)

    @staticmethod
    async def create_account(new_account : Account, company_id : int) -> Account:
        sqlaccount = await SQLAccountManger.get_SQLAccount_with_email(new_account.email)
        if sqlaccount is not None: raise Exception()
        sqlaccount = account_to_sqlaccount(new_account)
        sqlaccount.password_hash = get_password_hash(new_account.password)
        sqlaccount.company_id = company_id
        await SQLAccountManger.save_SQLAccount(sqlaccount)
        return sqlaccount_to_account_info(sqlaccount)

    def get_account_info(self) -> AccountInfo:
        return sqlaccount_to_account_info(self._sql_account)

    async def delete(self):
        await SQLAccountManger.SQLAccountManger.delete_SQLAccount(self._sql_account)

    def modify(self, account : Account) -> AccountInfo:
        # TODO implement
        ...
