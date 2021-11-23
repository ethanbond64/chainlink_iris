from flask import  request, Blueprint, jsonify, make_response
from server.blueprints.main.models import Event, Entry
from flask_cors import CORS
import datetime


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
                expiration=read_js_date(request.form.get("expiration_date")))

        event.save()

        resp['success'] = True
    return make_response(jsonify(resp),200)


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


from flask import render_template
from server.blueprints.main.models import Event
from server.utils.extensions import socketio
from flask_socketio import emit
# from server.blueprints.main.views import main
from server.blueprints.main.time_handler import img_to_bin
from server.blueprints.main.data_manager import save_event_record

from PIL import Image
from io import BytesIO 
import base64
import numpy as np

# Time authenticator route
@main.route('/timebox',methods=['GET'])
def view_timebox():
    return render_template('timebox.html')

# Video frame route
@main.route('/stream/<event_id>',methods=['GET'])
def stream_video(event_id):
    return render_template('index.html',event_id=event_id)

@main.route('/V1/latest/<event_id>')
def latest_entries(event_id):
    payload = {"entries":[e.json() for e in Entry.query.filter(Entry.event_id==event_id).order_by(Entry.timestamp.desc()).limit(5)]}
    return make_response(jsonify(payload),200)

# TODO 
# RT all between timestamps
# RT specfic timestamp
# RT require x confirmations


@socketio.on('VideoStreamIn', namespace='/iris')
def stream_in(data):
    print("VIDEO STREAM RECIEVED")
    print(data)
    
    data_url = data["DataURL"]
    event_id = data["EventID"]
    device_id = data["DeviceID"]

    # get event
    event = Event.query.filter(Event.id==event_id).first()

    if event is None :
        # TODO handle errors via socketIO
        emit('VideoStreamReceived', {'Valid': False}, namespace='/iris')
    # Process and save data
    img = stringToImage(data_url.split(",")[1])
    save_event_record(img,device_id,event)
 
    emit('VideoStreamReceived', {'Valid': True}, namespace='/iris')

@socketio.on('connect', namespace='/iris')
def test_connect():
    print("SOCKETIO CONNECTED")

def stringToImage(base64_string):
    imgdata = base64.b64decode(base64_string)
    return np.array(Image.open(BytesIO(imgdata)))


def read_js_date(datestring):
    return datetime.datetime.strptime(datestring, "%a, %d %b %Y %H:%M:%S %Z")