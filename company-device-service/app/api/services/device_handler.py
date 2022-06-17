from app.api.models.models.device_models import DeviceData, DeviceInfo, DeviceSearchFilter, Devices
from schemas.device_mongo_models.device_models import MongoDevice
from typing import List
from app.api.models.models.device_models import DeviceInfo, DeviceSearchFilter, Devices
from app.api.models.models.device_models import DeviceData, Measurement
import datetime

def mongo_device_to_device_data(mongo_device : MongoDevice, measurement_period_type : str) -> DeviceData:
    def unix_to_date(unix : int) -> str:
        dt = datetime.datetime.fromtimestamp(unix)
        return str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second)

    device : DeviceData = DeviceData.construct()
    device.creation_date = mongo_device.creation_date
    device.warning_level = str(mongo_device.warning_level)
    device.warning_level_height_mm = mongo_device.warning_level_height
    if measurement_period_type == 'all':
        device.measurements = [Measurement(time_s = unix_to_date(measurement.time_s), distance_mm = measurement.distance_mm) for measurement in mongo_device.data]
    if measurement_period_type == 'day':
        device.measurements = [Measurement(time_s = unix_to_date(measurement.time_s), distance_mm = measurement.distance_mm) for measurement in mongo_device.past_day_data]
    if measurement_period_type == 'week':
        device.measurements = [Measurement(time_s = unix_to_date(measurement.time_s), distance_mm = measurement.distance_mm) for measurement in mongo_device.past_week_data]
    if measurement_period_type == 'month':
        device.measurements = [Measurement(time_s = unix_to_date(measurement.time_s), distance_mm = measurement.distance_mm) for measurement in mongo_device.past_month_data]
    if measurement_period_type == 'year':
        device.measurements = [Measurement(time_s = unix_to_date(measurement.time_s), distance_mm = measurement.distance_mm) for measurement in mongo_device.past_year_data]
    device.device_id = mongo_device.id
    device.latitude = mongo_device.location.coordinates[0]
    device.longitude = mongo_device.location.coordinates[1]
    device.comments = mongo_device.comments
    device.installation_comment = mongo_device.installation_comment
    return device

def mongo_device_to_device_info(mongo_device : MongoDevice) -> DeviceInfo:
    device_info : DeviceInfo = DeviceInfo.construct()
    device_info.latitude = mongo_device.location.coordinates[0]
    device_info.longitude = mongo_device.location.coordinates[1]
    device_info.creation_date = mongo_device.creation_date
    device_info.warning_level = str(mongo_device.warning_level)
    device_info.warning_level_height_mm = mongo_device.warning_level_height_mm
    device_info.device_id = str(mongo_device.id)
    device_info.pinned = mongo_device.pinned
    device_info.installation_comment = mongo_device.installation_comment
    return device_info

def mongo_devices_to_devices(mongo_devices : List[MongoDevice], filter : DeviceSearchFilter) -> Devices:
    devices = Devices.construct()
    devices.search_filter = filter
    devices.devices = [mongo_device_to_device_info(mongo_device) for mongo_device in mongo_devices]
    return devices

class DeviceHandler:

    _mongo_device : MongoDevice

    async def __init__(self, company_id : int, device_id : str):
        device = await MongoDevice.get(id = device_id, company_id = company_id)
        # TODO add exception handling
        self._mongo_device = device

    @staticmethod
    async def get_devices(device_filter : DeviceSearchFilter, company_id : int) -> Devices:
        print('getting devices')
        if device_filter.warning_level is not None:
            mongo_devices = await MongoDevice.find(company_id = company_id).find(
                MongoDevice.warning_level == int(device_filter.warning_level)
            ).to_list()
        else:
            print(company_id,'acas')
            company_id = int(company_id)
            mongo_devices = await MongoDevice.find(MongoDevice.company_id == company_id).to_list()
        print(mongo_devices)
        # TODO add more filters
        return mongo_devices_to_devices(mongo_devices, device_filter)

    def get_device_data(self, measurement_period_type : str) -> DeviceData:
        return mongo_device_to_device_data(self._mongo_device, measurement_period_type)

    async def modify(self, new_device : DeviceInfo) -> DeviceInfo:
        self._mongo_device.comments = new_device.comments
        self._mongo_device.warning_level_height_mm = new_device.warning_level_height_mm
        await self._mongo_device.save_changes()
        return mongo_device_to_device_info(self._mongo_device)

    async def delete(self):
        await self._mongo_device.delete()
