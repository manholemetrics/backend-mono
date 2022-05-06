from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker 
from app.api.configs.configs import environmentSettings
from app.api.sqlalchemy_models.models import Base, SQLAccount, SQLCompany, SQLPermissions
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)
    #     await conn.run_sync(Base.metadata.create_all)

engine = create_async_engine(environmentSettings.database_url)
Session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

def create(klass):
    if not (klass.__tablename__ in inspect(engine).get_table_names()): 
        klass.__table__.create(bind = engine, checkfirst = True)

create(SQLCompany)
create(SQLPermissions)
create(SQLAccount)
session = Session()