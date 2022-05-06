from app.api.mongo_models.device_models import MongoDeviceDataEntry
from app.api.schemas.generated_models.queue_input.data_submission import DataEntry


def request_data_entry_to_mongo_data_entry(entry : DataEntry) -> MongoDeviceDataEntry:
    responseEntry : MongoDeviceDataEntry = MongoDeviceDataEntry.construct()
    responseEntry.time_s = entry.time
    responseEntry.distance_mm = entry.distance
    return responseEntry