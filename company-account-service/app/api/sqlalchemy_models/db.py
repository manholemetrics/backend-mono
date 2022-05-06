from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker 
from app.api.configs.configs import environmentSettings
from app.api.sqlalchemy_models.models import Base, SQLAccount, SQLCompany, SQLPermissions

print(environmentSettings.database_url)
engine = create_engine(environmentSettings.database_url)
Session = sessionmaker(bind=engine)

# if not engine.has_table(engine, SQLCompany):  # If table don't exist, Create.
#     Base.metadata.create_all(engine)
def create(klass):
    if not (klass.__tablename__ in inspect(engine).get_table_names()): 
        klass.__table__.create(bind = engine, checkfirst = True)

create(SQLCompany)
create(SQLPermissions)
create(SQLAccount)
session = Session()