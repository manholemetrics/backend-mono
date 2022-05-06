from app.api.models.models.account_models import Permissions
from app.api.sqlalchemy_models.models import SQLPermissions

def sqlpermissions_to_permissions(sqlpermission : Permissions) -> Permissions:
    ''' Map SQLPermissions to Permissions using dictionary constructor'''
    return Permissions(**sqlpermission.__dict__)

def permissions_to_sqlpermissions(permissions : Permissions) -> SQLPermissions:
    '''Map permission to SQLPermission by unpacking dictionary'''
    return SQLPermissions(**permissions.__dict__)