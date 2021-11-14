from server.utils.extensions import db
from server.utils.BaseModel import BaseModel
from sqlalchemy.dialects.postgresql import JSON

class Event(BaseModel,db.Model):

    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(100))
    about = db.Column(db.String(1000))

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

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), index=True, nullable=False)

    data = db.Column(JSON)