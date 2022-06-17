from app.api.sqlalchemy_models.models import SQLCompany, SQLAccount, SQLPermissions
from app.api.sqlalchemy_models.db import engine, async_session_maker
from sqlalchemy.orm import sessionmaker, selectinload 
from sqlalchemy.future import select

Session = sessionmaker(bind=engine)

class SQLAccountManger:
    

    @staticmethod
    async def get_SQLAccount(account_id : int, company_id : int) -> SQLAccount:
        async with async_session_maker() as session:
            company = await session.query(SQLAccount).filter_by(id = account_id, company_id = company_id).first()
        return company

    @staticmethod
    async def get_SQLAccount_with_email(email : int) -> SQLAccount:
        async with async_session_maker() as session:
            # company = await session.query(SQLAccount).filter_by(email = email).first()
            account = (await session.execute(select(SQLAccount).options(selectinload(SQLAccount.permissions)).where(SQLAccount.email == email).limit(1)))
            if account is not None: 
                account = account.scalars().first()
                if account is not None:
                    print(account.permissions)
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
        async with async_session_maker() as session:
            session.delete(account)
            await session.commit()

class SQLCompanyManager:

    @staticmethod
    async def get_SQLCompany(company_id : int) -> SQLCompany:
        async with async_session_maker() as session:
            company = await session.query(SQLCompany).filter_by(id = company_id).first()
        return company

    @staticmethod
    async def save_SQLCompany(company : SQLCompany):
        async with async_session_maker() as session:
            session.add(company)
            await session.commit()