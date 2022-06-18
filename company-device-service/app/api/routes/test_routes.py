# from xmlrpc.client import Boolean
# from fastapi.param_functions import Body
# from app.api.authentication.authentication import TokenData, token_authentication
# from app.api.exceptions.authentication_exception import InvalidPermissionException
# from app.api.main import app
# from fastapi.params import Depends
# from app.api.models.models.device_models import Device, DeviceData, DeviceInfo, DeviceSearchFilter, Devices, SetupInfo
# from app.api.services.handlers.device_handler import change_setup_status, delete_mongo_device, get_device_data_from_id, get_devices_with_filter, modify_device, register_device
# from app.api.device_mongo_models.device_models import MongoDevice
# from app.api.device_mongo_models.device_models import MongoDeviceDataEntry
# import time
# import uuid
# import datetime
# from pydantic import BaseModel, Field


# class DeviceMeasurement(BaseModel):
#     device_id : str
#     distance_mm : float = Field(description="distance measured by the sensor in mm")

# @app.post('/data', tags = ["Tests"])
# async def add_data(measurement : DeviceMeasurement = Body(...)):
#     device : MongoDevice = MongoDevice.objects(oid = measurement.device_id).first()
#     entry = MongoDeviceDataEntry()
#     entry.time_s = int(time.time())
#     entry.distance_mm = measurement.distance_mm
#     entry.oid = str(uuid.uuid1())
#     device.data.append(entry)
#     device.save()
#     return

# @app.get('/create_device', tags = ["Tests"])
# async def create_device():
#     print("hello")
#     '''Creates a fake device'''
#     # create 3 devices
#     mongo_device = MongoDevice()
#     mongo_device.company_id = "1"
#     mongo_device.creation_date = int(time.time())
#     mongo_device.location = [51.499782, -0.174437]
#     mongo_device.warning_level_height = 10
#     mongo_device.oid = "1"
#     mongo_device.warning_level = 5
#     mongo_device.data = []#[entry_0, entry_1, entry_2]
#     mongo_device.save()

#     mongo_device = MongoDevice()
#     mongo_device.company_id = "1"
#     mongo_device.creation_date = int(time.time())
#     mongo_device.location = [51.500009, -0.175456]
#     mongo_device.warning_level_height = 10
#     mongo_device.oid = "2"
#     mongo_device.warning_level = 7
#     entry_0 = MongoDeviceDataEntry()
#     entry_0.time_s = 1646740712
#     entry_0.distance_mm = 10
#     entry_1 = MongoDeviceDataEntry()
#     entry_1.time_s = 1646740719
#     entry_1.distance_mm = 10
#     entry_2 = MongoDeviceDataEntry()
#     entry_2.time_s = 1646740726
#     entry_2.distance_mm = 10
#     entry_0.oid = str(uuid.uuid1())
#     entry_1.oid = str(uuid.uuid1())
#     entry_2.oid = str(uuid.uuid1())
#     mongo_device.data = [entry_0, entry_1, entry_2]
#     mongo_device.save()

#     mongo_device = MongoDevice()
#     mongo_device.company_id = "1"
#     mongo_device.creation_date = int(time.time())
#     mongo_device.location = [51.498900, -0.176572]
#     mongo_device.warning_level_height = 10
#     mongo_device.oid = "3"
#     mongo_device.warning_level = 3
#     entry_0 = MongoDeviceDataEntry()
#     entry_0.time_s = 1646740712
#     entry_0.distance_mm = 10
#     entry_1 = MongoDeviceDataEntry()
#     entry_1.time_s = 1646740719
#     entry_1.distance_mm = 15
#     entry_2 = MongoDeviceDataEntry()
#     entry_2.time_s = 1646740726
#     entry_2.distance_mm = 20
#     entry_0.oid = str(uuid.uuid1())
#     entry_1.oid = str(uuid.uuid1())
#     entry_2.oid = str(uuid.uuid1())
#     mongo_device.data = [entry_0, entry_1, entry_2]
#     mongo_device.save()
#     return

    
from schemas.device_mongo_models.device_models import GeoJson2DPoint, MongoDevice
from app.api.main import app

@app.get('/create_device', tags = ["Tests"])
async def create_device():
    device = MongoDevice.construct()
    device.data = []
    device.past_day_data = [] 
    device.past_week_data = []
    device.past_month_data = []
    device.past_year_data = []
    device.company_id = 0
    device.creation_date = 0
    device.location = GeoJson2DPoint(coordinates=(51.500,-0.1743))
    device.warning_level = 5
    device.warning_level_height_mm  = 50
    device.installation_comment = ''
    device.comments = []
    device.pinned = False
    await device.save()
    print('saved')
    
    device = MongoDevice.construct()
    device.data = []
    device.past_day_data = [] 
    device.past_week_data = []
    device.past_month_data = []
    device.past_year_data = []
    device.company_id = 0
    device.creation_date = 0
    device.location = GeoJson2DPoint(coordinates=(51.498,-0.1832))
    device.warning_level = 5
    device.warning_level_height_mm  = 50
    device.installation_comment = ''
    device.comments = []
    device.pinned = False
    await device.save()
    print('saved')