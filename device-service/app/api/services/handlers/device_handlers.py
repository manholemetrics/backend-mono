import math
from app.api.schemas.generated_models.queue_input.data_submission import DataSubmission
from app.api.mongo_models.device_models import MongoDevice
from app.api.schemas.generated_models.queue_output.update_device_info_request import UpdateDeviceInfo
from app.api.services.mappers.request_data_entry_to_mongo_data_entry import request_data_entry_to_mongo_data_entry
from app.api.main import broker
from app.api.configs.configs import queueConfig

def _send_message_to_company_service(device_id : int, min_distance : int):
    updateDeviceInfo = UpdateDeviceInfo()
    updateDeviceInfo.device_id = device_id
    updateDeviceInfo.min_distance = min_distance
    broker.send(queueConfig.device_info_request,updateDeviceInfo)

def handle_data_submission_request(message : DataSubmission):
    try: device : MongoDevice = MongoDevice.objects(oid = message.device_id).first()
    except: raise Exception(detail = "Device Not Found")
    min_distance = math.inf
    for entry in message.data_entries:
        if entry.distance > min_distance: min_distance = entry.distance
        device.data.append(request_data_entry_to_mongo_data_entry(entry))
    device.save()
    _send_message_to_company_service(message.device_id,min_distance)
    return