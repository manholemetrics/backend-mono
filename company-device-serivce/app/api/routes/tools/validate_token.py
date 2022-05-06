from app.api.exceptions.authentication_exception import InvalidPermissionException


def validate_token(permission : bool, tokenData):
    if not permission: raise InvalidPermissionException(tokenData,"")