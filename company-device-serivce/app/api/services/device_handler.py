from app.api.models.models.device_models import Device, DeviceData, DeviceInfo, DeviceSearchFilter, Devices


class DeviceHandler:

    _device_filter : DeviceSearchFilter
    _mongo_device : Device
