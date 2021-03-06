from flask import  request, Blueprint, jsonify, make_response
from server.blueprints.main.models import Event, Entry
from flask_cors import CORS
import datetime
import json


main = Blueprint('main', __name__,template_folder='templates')
CORS(main,origins="http://localhost:3000")

# GET ENDPOINTS
@main.route('/test',methods=['GET'])
def get_test():
    return make_response(jsonify({"Test":True}),200)

@main.route('/get/events',methods=['GET'])
def get_events():

    events = Event.query.order_by(Event.created_on.desc()).all()
    resp = {"events":[event.json() for event in events]}

    return make_response(jsonify(resp),200)

@main.route('/create/event',methods=['POST'])
def create_entry():
    resp = {"success":False}
    if request.form.get("name") is not None:
        event = Event(
                name=request.form.get("name"),
                about=request.form.get("description"),
                start_time=request.form.get("start"),
                expiration=request.form.get("end"),
                dataPolicy=json.loads(request.form.get("policies")))

        event.save()

        resp['success'] = True
    return make_response(jsonify(resp),200)


# NOTE this is for non video data, posted in manually, not streamed
@main.route('/create/entry',methods=['POST'])
def create_event():
    resp = {"success":False}
    if request.form.get("event_id") is not None:
        event = Event.query.filter(Event.id==request.form.get("event_id")).first()
        if event is not None:
            # TODO validate data matches policy
            entry = Entry(event_id=request.form.get("event_id"),data=request.form.get("data"))
            entry.save()
            resp['success'] = True
    
    return make_response(jsonify(resp),200)


@main.route('/get/entries/<event>',methods=['GET'])
def get_entries(event):

    entries = Entry.query.filter(Entry.event_id==event).order_by(Entry.created_on.desc()).all()
    resp = {"entries":[entry.json() for entry in entries]}

    return make_response(jsonify(resp),200)

@main.route('/get/contracts/<event>',methods=['GET'])
def get_contracts(event):

    # entries = Entry.query.filter(Entry.event_id==event).order_by(Entry.created_on.desc()).all()
    # resp = {"entries":[entry.json() for entry in entries]}

    return make_response(jsonify({"contracts":[1,2,3]}),200)