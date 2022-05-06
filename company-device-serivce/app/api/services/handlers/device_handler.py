import time
from typing import List
from app.api.exceptions.not_found_exception import DeviceNotFoundException
from app.api.models.models.device_models import Device, DeviceData, DeviceInfo, DeviceSearchFilter, Devices, SetupInfo
from app.api.device_mongo_models.device_models import MongoDevice
from app.api.services.mappers.device_to_mongo_device import device_to_mongo_device
from app.api.services.mappers.mongo_device_to_device_data import mongo_device_to_device_data
from app.api.services.mappers.mongo_device_to_device_info import mongo_device_to_device_info
from app.api.services.mappers.mongo_devices_to_devices import mongo_devices_to_devices

def get_device_data_from_id(_id : str, start_index : int, end_index : int, company_id : str) -> DeviceData:
    #print(company_id)
    #print(_id)
    #device = MongoDevice.objects(slice__data = [start_index,end_index]).first()
    #print(device.company_id)
    try: device : MongoDevice = MongoDevice.objects(oid = _id, 
        company_id = company_id, 
        #slice__data = [start_index,end_index]
    ).first()
    except: raise DeviceNotFoundException(_id)
    print(device)
    return mongo_device_to_device_data(device)

def get_devices_with_filter(filter : DeviceSearchFilter, company_id : str) -> Devices:
    filter_object = {"company_id": company_id}
    print(company_id)
    if filter.warning_level is not None: 
        filter_object["warning_level"] = filter.warning_level
    if filter.latitude is not None and filter.longitude is not None and filter.distance is not None:
        filter_object["location__geo_within_center"] = [(filter.latitude, filter.longitude), filter.distance]
    print(filter)
    mongo_devices : List[MongoDevice] = MongoDevice.objects(**filter_object).exclude("data")[filter.start_index: filter.end_index]
    return mongo_devices_to_devices(mongo_devices, filter)

def modify_device(device : Device, company_id : str) -> DeviceInfo:
    mongo_device = device_to_mongo_device(device, company_id)
    mongo_device.setup_complete = False
    mongo_device.save()
    device_info = mongo_device_to_device_info(mongo_device)
    return device_info

def register_device(device : Device, company_id : str) -> DeviceInfo:
    try: device : MongoDevice = MongoDevice.objects(oid = device._id, company_id = "").first()
    except: raise DeviceNotFoundException(device._id)
    if device == None: DeviceNotFoundException(device._id) # change to custom exception
    mongo_device = device_to_mongo_device(device, company_id)
    mongo_device.setup_complete = False
    mongo_device.save()
    device_info = mongo_device_to_device_info(mongo_device)
    return device_info

def get_setup_height(device_id : str, company_id : str) -> SetupInfo:
    try: device : MongoDevice = MongoDevice.objects(oid = device_id, company_id = company_id).first()
    except: raise DeviceNotFoundException(device_id)
    if device == None: DeviceNotFoundException(device_id)
    info = SetupInfo.construct()
    info.height = device.setup_height
    return info

def change_setup_status(device_id : str, setup : bool, company_id : str):
    try: device : MongoDevice = MongoDevice.objects(oid = device_id, company_id = company_id).first()
    except: raise DeviceNotFoundException(device_id)
    if device == None: DeviceNotFoundException(device_id)
    device.setup_complete = True
    device.save()
    device_info = mongo_device_to_device_info(device)
    return device_info

def delete_mongo_device(device_id : str, company_id : str):
    try: device : MongoDevice = MongoDevice.objects(oid = device_id, company_id = company_id).first()
    except: raise DeviceNotFoundException(device_id)
    if device == None: DeviceNotFoundException(device_id)
    device.delete()