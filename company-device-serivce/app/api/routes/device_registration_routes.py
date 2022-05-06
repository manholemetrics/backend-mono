from fastapi.param_functions import Body
from app.api.authentication.authentication import TokenData, token_authentication
from app.api.main import app
from fastapi.params import Depends
from app.api.models.models.device_models import Device, DeviceInfo, SetupInfo
from app.api.routes.tools.validate_token import validate_token
from app.api.services.handlers.device_handler import change_setup_status, register_device

@app.get('/setup_height', response_model=SetupInfo, tags=["Device Registration"])
async def get_setup_height(device_id : str, tokenData : TokenData = Depends(token_authentication)) -> SetupInfo:
    '''Returns the current height being read by the device'''
    validate_token(tokenData.permission.view_device_data, tokenData)
    return get_setup_height(device_id, tokenData.company_id)

@app.put('/device_setup', response_model=DeviceInfo, tags=["Device Registration"])
async def put_device(device_id : str, setup : bool, tokenData : TokenData = Depends(token_authentication)) -> DeviceInfo:
    '''Change the device setup status'''
    validate_token(tokenData.permission.manage_devices, tokenData)
    return change_setup_status(device_id, setup, tokenData.company_id)

@app.post('/device', response_model=DeviceInfo, tags=["Device Registration"])
async def post_device(device : Device = Body(...), tokenData : TokenData = Depends(token_authentication)) -> DeviceInfo:
    '''Allows registration of a new Device'''
    validate_token(tokenData.permission.register_devices, tokenData)
    return register_device(device, tokenData.company_id)