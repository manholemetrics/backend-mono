# from mongoengine import Document
# from mongoengine.document import EmbeddedDocument
# from mongoengine.fields import EmbeddedDocumentField, GeoPointField, IntField, ListField, StringField

# class MongoDeviceDataEntry(EmbeddedDocument):
#     oid = IntField(required=True, primary_key=True)
#     time_s = IntField(required=True)
#     distance_mm = IntField(required=True)

# class MongoDevice(Document):
#     oid = StringField(required=True, primary_key=True)
#     data = ListField(EmbeddedDocumentField(MongoDeviceDataEntry))
#     company_id = StringField(required=True)
#     creation_date = IntField(required=True)
#     location = GeoPointField(required=True)
#     warning_level = IntField()
#     warning_level_height = IntField(required = True)

# class Company(Document):
#     oid = StringField(required=True, primary_key=True)
    
from typing import Optional, Tuple
from pydantic import BaseModel
from beanie import Document, Indexed, init_beanie
import asyncio, motor
import pymongo

class GeoJson2DPoint(BaseModel):
    type: str = "Point"
    coordinates: Tuple[float, float]

class MongoDeviceDataEntry(BaseModel):
    time_s : int
    distance_mm : int

class MongoDevice(Document):
    class DocumentMeta:
      collection_name = "mongo-devices"
    data : list[MongoDeviceDataEntry]
    past_day_data : list[MongoDeviceDataEntry]
    past_week_data : list[MongoDeviceDataEntry]
    past_month_data : list[MongoDeviceDataEntry]
    past_year_data : list[MongoDeviceDataEntry]
    company_id : int
    creation_date : int
    location : GeoJson2DPoint
    warning_level : int
    warning_level_height_mm : int
    # any comments made at the point of installation
    installation_comment : str = ''
    # comments made on the device
    comments : list[str]
    pinned : bool = False
    
    class Collection:
        name = "places"
        indexes = [
            [("location", pymongo.GEOSPHERE)],  # GEO index
        ]
    
    

MongoDevice.update_forward_refs()
