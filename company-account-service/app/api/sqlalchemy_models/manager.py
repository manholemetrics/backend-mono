from app.api.sqlalchemy_models.models import SQLCompany, SQLAccount, SQLPermissions
from app.api.sqlalchemy_models.db import engine, async_session_maker
from sqlalchemy.orm import sessionmaker, selectinload , subqueryload, joinedload
from sqlalchemy.future import select

Session = sessionmaker(bind=engine)

class SQLAccountManger:
    

    @staticmethod
    async def get_SQLAccount(account_id : int, company_id : int) -> SQLAccount:
        async with async_session_maker() as session:
            account_id = int(account_id)
            company_id = int(company_id)
            account = (await session.execute(select(SQLAccount).options(selectinload(SQLAccount.permissions)).where(SQLAccount.account_id == account_id, SQLAccount.company_id == company_id).limit(1)))
            if account is not None: 
                account = account.scalars().first()
        return account

    @staticmethod
    async def get_SQLAccount_with_email(email : int) -> SQLAccount:
        async with async_session_maker() as session:
            # company = await session.query(SQLAccount).filter_by(email = email).first()
            account = (await session.execute(select(SQLAccount).options(selectinload(SQLAccount.permissions)).where(SQLAccount.email == email).limit(1)))
            if account is not None: 
                account = account.scalars().first()
            print(account)
        return account 

    @staticmethod
    async def save_SQLAccount(account : SQLAccount):
        async with async_session_maker() as session:
            print('adding account') 
            session.add(account)
            await session.commit()
            print('added acount')

    @staticmethod
    async def delete_SQLAccount(account : SQLAccount):
        print('deleeting')
        async with async_session_maker() as session:
            await session.delete(account)
            await session.commit()

class SQLCompanyManager:

    @staticmethod
    async def get_SQLCompany(company_id : int) -> SQLCompany:
        async with async_session_maker() as session:
            company_id = int(company_id)
            company = (await session.execute(select(SQLCompany).options(joinedload(SQLCompany.accounts).subqueryload(SQLAccount.permissions)).where(SQLCompany.company_id == company_id).limit(1)))
            if company is not None: 
                company = company.scalars().first()
        return company

    @staticmethod
    async def save_SQLCompany(company : SQLCompany):
        async with async_session_maker() as session:
            session.add(company)
            await session.commit()