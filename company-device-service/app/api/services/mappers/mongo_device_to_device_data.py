from app.api.models.models.device_models import DeviceData, Measurement
from schemas.device_mongo_models.device_models import MongoDevice
import datetime
from typing import List


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