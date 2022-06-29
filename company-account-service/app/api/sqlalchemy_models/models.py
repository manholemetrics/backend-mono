from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Integer, String

# TODO add in device setup requests
#   - should contain location information and date information and completion status and device id if completed

Base = declarative_base()
# metadata = Base.metadata

class SQLCompany(Base):
    __tablename__ = 'sqlcompanies'
    company_id = Column(Integer, primary_key=True, autoincrement=True)
    accounts = relationship("SQLAccount", backref="company")
    

class SQLAccount(Base):
    __tablename__ = 'sqlaccounts'
    account_id = Column(Integer, primary_key=True, autoincrement=True)
    permissions = relationship("SQLPermissions", uselist=False, backref="account", cascade = "all, delete, delete-orphan" )
    company_id = Column(Integer, ForeignKey('sqlcompanies.company_id'))
    email = Column(String(100))
    password_hash = Column(String(100))
    password_salt = Column(String(100))

class SQLPermissions(Base):
    __tablename__ = 'sqlpermissions'
    permissions_id = Column(Integer, primary_key=True, autoincrement=True)
    view_devices = Column(Boolean)
    register_devices = Column(Boolean)
    manage_devices = Column(Boolean)
    manage_accounts = Column(Boolean)
    view_device_data = Column(Boolean)
    account_id = Column(Integer, ForeignKey('sqlaccounts.account_id', use_alter=True))