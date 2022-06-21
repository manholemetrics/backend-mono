from app.api.main import app
from schemas.device_mongo_models.device_models import MongoDevice, MongoDeviceDataEntry
import time
from fastapi import Body
from app.api.tasks.update_average_measurements import process_average_measurements_task

from pydantic import BaseModel

from Crypto.PublicKey import RSA
import json

class Payload(BaseModel):
    payload : str
    device_id : str
    

@app.post('/measurements', response_model=str, tags=["Measurements"])
async def post_measurements(payload : Payload = Body(...)) -> str:
    mongo_device = await MongoDevice.get(payload.device_id)
    payload = json.loads(str(RSA.importKey(mongo_device.decryption_key).decrypt(payload.payload)))
    
    for time_s, distance_mm in zip(payload['time_s'], payload['distance_mm']):
        entry = MongoDeviceDataEntry(time_s=time_s, distance_mm=distance_mm)
        mongo_device.data.append(entry)
    await mongo_device.save()
    
    response = {}
    response['atmega_settings'] = {
        'sleep_time_s' : mongo_device.sleep_time_s,
        'transmit_time_s' : mongo_device.transmit_time_s
    }
    response['esp_settings'] = {
        # 'auth_key' : None,
        # 'code_version' : None,
        # 'url' : None
    }
    
    # sends a task request to process average task updates
    process_average_measurements_task(payload.device_id)
    return json.dumps(response)

# need to allow for tasks that calculate the weekly and average routes
# need to sort out encryption system



# class Settings:

#     class ESPSettings:

#         code_version : str
#         auth_key : str
#         url : str
        
#         def __init__(self, settings : dict) -> None:
#             self.code_version = settings['code_version']
#             if 'auth_key' in settings: self.auth_key = settings['auth_key']
#             if 'url' in settings: self.url = settings['url']

#     class AtmegaSettings:

#         sleep_time_s : int
#         transmit_time_s : int
        
#         def __init__(self, settings : dict) -> None:
#             self.sleep_time_s = settings['sleep_time_s']
#             self.transmit_time_s = settings['transmit_time_s']

#     esp_settings : ESPSettings
#     atmega_settings : AtmegaSettings

#     def __init__(self, settings : dict):
#         self.esp_settings = Settings.ESPSettings(settings['esp_settings'])
#         self.atmega_settings = Settings.AtmegaSettings(settings['atmega_settings'])