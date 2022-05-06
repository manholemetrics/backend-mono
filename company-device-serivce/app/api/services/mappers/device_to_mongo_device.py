from app.api.device_mongo_models.device_models import MongoDevice
from app.api.models.models.device_models import Device
import time

def device_to_mongo_device(device : Device, company_id : str) -> MongoDevice:
    mongo_device = MongoDevice()
    mongo_device.company_id = company_id
    mongo_device.creation_date = int(time.time())
    mongo_device.location = [device.latitude, device.longitude]
    mongo_device.warning_level_height = device.warning_level_height
    mongo_device.oid = device._id
    return mongo_device