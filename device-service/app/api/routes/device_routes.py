from app.api.main import app
from app.api.models.models import Measurements, Response
from schemas.device_mongo_models.device_models import MongoDevice, MongoDeviceDataEntry
import time

# TODO should send back information for this device
@app.post('/measurements', response_model=Response, tags=["Measurements"])
async def post_measurements(measurement : Measurements) -> Response:
    response = Response.construct()
    response.time = int(time.time)
    mongo_device = await MongoDevice.get(measurement.device_id)
    for time_s, distance_mm in zip(measurement.time_s, measurement.distance_mm):
        entry = MongoDeviceDataEntry(time_s=time_s, distance_mm=distance_mm)
        mongo_device.data.append(entry)
    await mongo_device.save()
    return response
