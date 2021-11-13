import datetime
from server.utils.extensions import db

def get_datetime():

    return datetime.datetime.now()

class BaseModel(object):
    # Keep track when records are created and updated.
    created_on = db.Column(db.DateTime(),
                           default=get_datetime)
    updated_on = db.Column(db.DateTime(),
                           default=get_datetime,
                           onupdate=get_datetime)


    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        return db.session.commit()

    def json(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
