from app.api.device_mongo_models.device_models import MongoDevice
from app.api.models.models.device_models import DeviceInfo

def mongo_device_to_device_info(mongo_device : MongoDevice) -> DeviceInfo:
    device_info : DeviceInfo = DeviceInfo.construct()
    device_info.creation_date = mongo_device.creation_date
    device_info.latitude = mongo_device.location[0]
    device_info.longitude = mongo_device.longitude
    device_info.warning_level = str(mongo_device.warning_level)
    device_info.warning_level_height = mongo_device.warning_level_height
    device_info._id = mongo_device.oid
    return device_info