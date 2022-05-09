from typing import List
from schemas.device_mongo_models.device_models import MongoDevice
from app.api.models.models.device_models import DeviceInfo, DeviceSearchFilter, Devices

def mongo_device_to_device_info(mongo_device : MongoDevice) -> DeviceInfo:
    device_info : DeviceInfo = DeviceInfo.construct()
    device_info.latitude = mongo_device.location.coordinates[0]
    device_info.longitude = mongo_device.location.coordinates[1]
    device_info.creation_date = mongo_device.creation_date
    device_info.warning_level = str(mongo_device.warning_level)
    device_info.warning_level_height = mongo_device.warning_level_height
    device_info.number_measurements = len(mongo_device.data)
    device_info.device_id = mongo_device.oid
    return device_info

def mongo_devices_to_devices(mongo_devices : List[MongoDevice], filter : DeviceSearchFilter) -> Devices:
    devices = Devices.construct()
    devices.search_filter = filter
    devices.devices = [mongo_device_to_device_info(mongo_device) for mongo_device in mongo_devices]
    return devices