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
    
from typing import Optional
from pydantic import BaseModel
from beanie import Document, Indexed, init_beanie
import asyncio, motor

class GeoJson2DPoint(BaseModel):
    type: str = "Point"
    coordinates: tuple[float, float]

class MongoDeviceDataEntry(BaseModel):
    _id : int
    time_s : int
    distance_mm : int

class MongoDevice(Document):
    _id : str
    data : list[MongoDeviceDataEntry]
    company_id : str
    creation_date : int
    location : GeoJson2DPoint
    warning_level : int
    warning_level_height_mm : int