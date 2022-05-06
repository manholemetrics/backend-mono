from fastapi import Request
from fastapi.responses import JSONResponse
from app.api.main import app

class DeviceNotFoundException(Exception):
    def __init__(self, _id: str):
        self._id = _id

@app.exception_handler(DeviceNotFoundException)
async def device_not_found_exception_handler(request: Request, exc: DeviceNotFoundException):
    #TODO add logging code
    return JSONResponse(
        status_code=404,
        content={"_id": exc._id},
    )
