from app.api.sqlalchemy_models.models import SQLCompany, SQLAccount, SQLPermissions
from app.api.sqlalchemy_models.db import engine
from sqlalchemy.orm import sessionmaker 

Session = sessionmaker(bind=engine)

class SQLAccountManger:

    @staticmethod
    async def get_SQLAccount(account_id : int, company_id : int) -> SQLAccount:
        async with Session(engine) as session:
            company = await session.query(SQLAccount).filter_by(id = account_id, company_id = company_id).first()
        return company

    @staticmethod
    async def get_SQLAccount_with_email(email : int) -> SQLAccount:
        async with Session(engine) as session:
            company = await session.query(SQLAccount).filter_by(email = email).first()
        return company

    @staticmethod
    async def save_SQLAccount(account : SQLAccount):
        async with Session(engine) as session:
            session.add(account)
            await session.commit()

    @staticmethod
    async def delete_SQLAccount(account : SQLAccount):
        async with Session(engine) as session:
            session.delete(account)
            await session.commit()

class SQLCompanyManager:

    @staticmethod
    async def get_SQLCompany(company_id : int) -> SQLCompany:
        async with Session(engine) as session:
            company = await session.query(SQLCompany).filter_by(id = company_id).first()
        return company

    @staticmethod
    async def save_SQLCompany(company : SQLCompany):
        async with Session(engine) as session:
            session.add(company)
            await session.commit()