from mongoengine import Document
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentField, GeoPointField, IntField, ListField, StringField

class MongoDeviceDataEntry(EmbeddedDocument):
    oid = IntField(required=True, primary_key=True)
    time_s = IntField(required=True)
    distance_mm = IntField(required=True)

class MongoDevice(Document):
    oid = StringField(required=True, primary_key=True)
    data = ListField(EmbeddedDocumentField(MongoDeviceDataEntry))
    company_id = StringField(required=True)
    creation_date = IntField(required=True)
    location = GeoPointField(required=True)
    warning_level = IntField()
    warning_level_height = IntField(required = True)

class Company(Document):
    oid = StringField(required=True, primary_key=True)
    