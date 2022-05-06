from app.api.sqlalchemy_models.models import SQLCompany, SQLAccount, SQLPermissions
from app.api.sqlalchemy_models.db import engine

def get_SQLCompany(company_id : str) -> SQLCompany:
    with Session(engine) as session:
        company = session.query(SQLCompany).filter_by(id = company_id).first()
    return company

def save_company(company : SQLCompany):
    with Session(engine) as session:
        session.add(company)
        session.commit()

def get_SQLAccount(account_id : str, company_id : str) -> SQLAccount:
    with Session(engine) as session:
        company = session.query(SQLAccount).filter_by(id = account_id, company_id = company_id).first()
    return company


def get_SQLAccount_with_email(email : str) -> SQLAccount:
    with Session(engine) as session:
        company = session.query(SQLAccount).filter_by(email = email).first()
    return company


def save_SQLAccount(account : SQLAccount):
    with Session(engine) as session:
        session.add(account)
        session.commit()

def delete_SQLAccount(account : SQLAccount):
    with Session(engine) as session:
       
        session.delete(account)

        session.commit()


class SQLCompanyManager():

    def __init__(self, sqlCompany : SQLCompany) -> 'SQLCompanyManager':
        self.sqlCompany = sqlCompany
        return self

    @static
    def query_id(self, company_id : str) -> 'SQLCompanyManager':
        with Session(engine) as session:
            company = session.query(SQLCompany).filter_by(id = tokenData.company_id).first()
            self.sqlCompany = company
        return self

    def get_sqlcompany(self) -> SQLCompany:
        return self.sqlCompany