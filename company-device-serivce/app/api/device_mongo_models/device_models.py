from email.policy import default
from mongoengine import Document
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentListField, PointField, IntField, StringField, BooleanField

class MongoDeviceDataEntry(EmbeddedDocument):
    oid = StringField(required=True, primary_key=True)
    time_s = IntField(required=True)
    distance_mm = IntField(required=True)

class MongoDevice(Document):
    oid = StringField(required=True, primary_key=True)
    data = EmbeddedDocumentListField(MongoDeviceDataEntry)
    company_id = StringField(required=True, default = "")
    creation_date = IntField(required=True)
    location = PointField(required=True)
    warning_level = IntField()
    warning_level_height = IntField(required = True)
    setup_complete = BooleanField(required = True, default = False)
    setup_height = IntField(required = True, default = 0)

class Company(Document):
    oid = StringField(required=True, primary_key=True)
    