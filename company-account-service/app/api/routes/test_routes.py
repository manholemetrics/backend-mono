from app.api.authentication.authentication import Permissions
from app.api.main import app
from app.api.models.account_models import Account
from app.api.services.account_handler import AccountHandler
from app.api.sqlalchemy_models.models import SQLCompany
from app.api.sqlalchemy_models.db import async_session_maker
from sqlalchemy import insert

@app.get('/create_user', tags=["Test"])
async def get_create_user():
    '''Create a fake user and company, the user name and password are test'''
    async with async_session_maker() as session:
        sqlCompany : SQLCompany = SQLCompany()
        sqlCompany.company_id = 0
        print(session)
        print(async_session_maker)
        session.add(sqlCompany)
        await session.commit()
        account = Account.construct()
        account.email = "test"
        account.password = "test"
        account.company_id = sqlCompany.company_id
        permission : Permissions = Permissions.construct()
        permission.view_devices = True
        permission.register_devices = True
        permission.manage_devices  = True
        permission.manage_accounts  = True
        permission.view_device_data = True
        account.permission = permission
        await AccountHandler.create_account(account, 0)
        print('created')
        return