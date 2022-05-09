from app.api.models.models.device_models import Device, DeviceData, DeviceInfo, DeviceSearchFilter, Devices
from schemas.device_mongo_models.device_models import MongoDevice
from app.api.services.mappers.mongo_device_to_device_data import mongo_device_to_device_data
from app.api.services.mappers.mongo_devices_to_devices import mongo_devices_to_devices

class DeviceHandler:

    _mongo_device : MongoDevice

    async def __init__(self, company_id : int, device_id : str):
        device = await MongoDevice.get(id = device_id, company_id = company_id)
        # TODO add exception handling
        self._mongo_device = device

    @staticmethod
    async def get_devices(device_filter : DeviceSearchFilter, company_id : int):
        mongo_devices = await MongoDevice.find(company_id = company_id).find(
            MongoDevice.warning_level == int(device_filter.warning_level)
        )
        # TODO add more filters
        return mongo_devices_to_devices(mongo_devices)

    def get_device_data(self) -> DeviceData:
        return mongo_device_to_device_data(self._mongo_device)

    async def modify(self, new_device : Device) -> DeviceInfo:
        ...

    async def delete(self):
        ...
