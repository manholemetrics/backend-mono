from app.api.sqlalchemy_models.models import SQLCompany
from app.api.models.account_models import Accounts
from app.api.services.mappers.account_mapper import sqlaccount_to_account_info
import app.api.sqlalchemy_models.manager as db_manager 

class CompanyHandler:
    
    sql_company : SQLCompany
        
    @classmethod
    async def create(klass, company_id : int):
        sql_company = await db_manager.SQLCompanyManager.get_SQLCompany(company_id)
        handler =  klass()
        handler.sql_company = sql_company
        return handler

    def get_company_accounts_list(self) -> Accounts:
        accounts = Accounts.construct()
        accounts.accounts = [sqlaccount_to_account_info(account) for account in self.sql_company.accounts]
        return accounts






























