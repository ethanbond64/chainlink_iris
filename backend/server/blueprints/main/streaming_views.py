
from flask import render_template, Blueprint, make_response, jsonify
from server.blueprints.main.models import Event, Entry
from server.utils.extensions import socketio
from flask_socketio import emit
# from server.blueprints.main.views import main
from server.blueprints.main.time_handler import img_to_bin
from server.blueprints.main.data_manager import save_event_record
from server.blueprints.main.confirmation_handler import get_confirmations
from flask_cors import CORS
from PIL import Image
from io import BytesIO 
import base64
import numpy as np
import datetime

streaming = Blueprint('streaming', __name__,template_folder='templates')
CORS(streaming,origins="http://localhost:3000")

# Time authenticator route
@streaming.route('/timebox',methods=['GET'])
def view_timebox():
    return render_template('timebox.html')

# Video frame route
@streaming.route('/stream/<event_id>',methods=['GET'])
def stream_video(event_id):
    return render_template('index.html',event_id=event_id)


@streaming.route('/V1/latest/<event_id>')
def latest_entries(event_id):
    entry = Entry.query.filter(Entry.event_id==event_id).order_by(Entry.timestamp.desc()).first()
    payload = {
        "data":entry.data,
        "confirmations": get_confirmations(entry,event_id)
    }
    return make_response(jsonify(payload),200)

@streaming.route('/V1/raw/latest/<event_id>')
def latest_entries_raw(event_id):
    payload = {
        "entries":[ e.json() for e in 
            Entry.query.filter(Entry.event_id==event_id).order_by(Entry.timestamp.desc()).limit(5)
            ]
        }
    return make_response(jsonify(payload),200)

@streaming.route('/V1/raw/after/<date>/<event_id>')
def after_entries_raw(event_id,date):
    payload = {
        "entries":[ e.json() for e in 
            Entry.query.filter(Entry.event_id==event_id,Entry.timestamp>date).order_by(Entry.timestamp.desc()).limit(5)
            ]
        }
    return make_response(jsonify(payload),200)


@streaming.route('/V1/raw/before/<date>/<event_id>')
def before_entries_raw(event_id,date):
    payload = {
        "entries":[ e.json() for e in 
            Entry.query.filter(Entry.event_id==event_id,Entry.timestamp<date).order_by(Entry.timestamp.desc()).limit(5)
            ]
        }
    return make_response(jsonify(payload),200)


@streaming.route('/V1/raw/between/<date1>/<date2>/<event_id>')
def between_entries_raw(event_id,date1,date2):
    payload = {
        "entries":[ e.json() for e in 
            Entry.query.filter(Entry.event_id==event_id,Entry.timestamp<date1,Entry.timestamp>date2).order_by(Entry.timestamp.desc()).limit(5)
            ]
        }
    return make_response(jsonify({}),200)

# TODO 
# RT all between timestamps
# RT specfic timestamp
# RT require x confirmations


# TODO rate limit the frames as they come in, so there are not big chunks of time with 100+ entries
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