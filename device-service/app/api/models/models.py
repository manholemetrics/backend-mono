from pydantic import BaseModel, Field

class Measurements(BaseModel):
    time_s : list[int]
    distance_mm : list[int]
    device_id : str

class Response(BaseModel):
    time : int
