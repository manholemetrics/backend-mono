import time
from app.api.main import celery
from schemas.device_mongo_models.device_models import MongoDevice, MongoDeviceDataEntry


async def process_average_measurements(device_id : str):
    total_measurements_per_period = 24*15
    def average_list(data : list[MongoDeviceDataEntry]):
        measurements = []
        chunks = [data[x:x+total_measurements_per_period] for x in range(0, len(data), total_measurements_per_period)]
        for chunk in chunks:
            total_time = 0
            total_distance = 0
            for measurement in chunk:
                total_time += measurement.time_s
                total_distance += measurement.distance_mm
            total_time /= len(chunk)
            total_distance /= len(chunk)
            measurement.append(MongoDeviceDataEntry(total_time, total_distance))
        return measurements
    
    # TODO do this in a much better way
    mongo_device = await MongoDevice.get(device_id)
    data = MongoDevice.data
    last_day = []
    last_week = []
    last_month = []
    last_year = []
    for measurement in data:
        if measurement.time_s - int(time.time()) < (24*60*60):
            last_day.append(measurement)
        if measurement.time_s - int(time.time()) < (7*24*60*60):
            last_week.append(measurement)
        if measurement.time_s - int(time.time()) < (31*24*60*60):
            last_month.append(measurement)
        if measurement.time_s - int(time.time()) < (365*24*60*60):
            last_year.append(measurement)
    mongo_device.past_day_data = average_list(mongo_device.data)
    mongo_device.past_week_data = average_list(mongo_device.data)
    mongo_device.past_month_data = average_list(mongo_device.data)
    mongo_device.past_year_data = average_list(mongo_device.data)
    await mongo_device.save()
    
import asyncio
@celery.task(name="process_average_measurements_task")
def process_average_measurements_task(device_id : str):
    asyncio.run(process_average_measurements(device_id))