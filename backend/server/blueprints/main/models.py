from server.utils.extensions import db
from server.utils.BaseModel import BaseModel
# from sqlalchemy.dialects.postgresql import JSON

class Event(BaseModel,db.Model):

    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(100))
    about = db.Column(db.String(1000))

    expiration = db.Column(db.DateTime())

    # TODO data in/out policy
