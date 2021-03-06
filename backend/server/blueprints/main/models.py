from datetime import datetime
from server.utils.extensions import db
from server.utils.BaseModel import BaseModel
from sqlalchemy.dialects.postgresql import JSON

class Event(BaseModel,db.Model):

    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(100))
    about = db.Column(db.String(1000))

    start_time = db.Column(db.DateTime(),default=datetime.now())
    expiration = db.Column(db.DateTime())

    # keys are names, values are types
    # nested types nest
    dataPolicy = db.Column(JSON)
    # dataInPolicy = db.Column(JSON)
    # dataOutPolicy = db.Column(JSON)

    # Number of people that need to submit confirming data for it to be true
    required_confirmations = db.Column(db.Integer)

class Entry(BaseModel,db.Model):

    __tablename__ = 'entries'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    data = db.Column(JSON)
    timestamp = db.Column(db.DateTime(),index=True)
    device_signature = db.Column(db.String(128))



class Contract(BaseModel,db.Model):

    __tablename__ = "contracts"

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    env_json = db.Column(JSON)
    filename = db.Column(db.String(100))
    deployed = db.Column(db.Boolean,default=False)
