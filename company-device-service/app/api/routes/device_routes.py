from fastapi.param_functions import Body
from app.api.authentication.authentication import TokenData, token_authentication
from app.api.exceptions.authentication_exception import InvalidPermissionException
from app.api.main import app
from fastapi.params import Depends
from app.api.models.models.device_models import Device, DeviceData, DeviceInfo, DeviceSearchFilter, Devices
from app.api.routes.tools.validate_token import validate_token
from app.api.services.device_handler import DeviceHandler

# working
@app.get('/devices', response_model=Devices, tags=["Device Info"])
async def get_devices(device_filter : DeviceSearchFilter = Depends(), tokenData : TokenData = Depends(token_authentication)) -> Devices:
    print(device_filter)
    '''Request a list of Devices, can use filters such as nearest to a coordinate or at a certain warning level, requires view_devices permission'''
    validate_token(tokenData.permission.view_devices, tokenData)
    devices = await DeviceHandler.get_devices(device_filter, tokenData.company_id)
    return devices

# working
@app.get('/device', response_model=DeviceData, tags=["Device Info"])
async def get_device(device_id : str, measurement_period_type : str,
    tokenData : TokenData = Depends(token_authentication)) -> DeviceData:
    '''Request a specific Device, requires view_device_data permission'''
    validate_token(tokenData.permission.view_device_data, tokenData)
    handler = await DeviceHandler.create(tokenData.company_id, device_id)
    return handler.get_device_data(measurement_period_type)

# working
@app.put('/device', response_model=DeviceInfo, tags=["Device Info"])
async def put_device(device : Device = Body(...), tokenData : TokenData = Depends(token_authentication)) -> DeviceInfo:
    '''Allows modification of a device, requires manage_device permission'''
    validate_token(tokenData.permission.manage_devices, tokenData)
    handler = await DeviceHandler.create(tokenData.company_id, device.device_id)
    return await handler.modify(device)


@app.delete('/device', tags=["Device Info"])
async def delete_device(device_id : str, tokenData : TokenData = Depends(token_authentication)):
    '''Requires manage_device permission'''
    validate_token(tokenData.permission.manage_devices, tokenData)
    return DeviceHandler(tokenData.company_id, device_id).delete()