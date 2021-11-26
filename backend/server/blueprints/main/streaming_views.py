
from flask import json, render_template, Blueprint, make_response, jsonify, request
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
import cv2

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
    entry = Entry.query.filter(Entry.event_id==event_id,Entry.timestamp!=None).order_by(Entry.timestamp.desc()).first()
    payload = {
        "data":entry.data,
        "confirmations": get_confirmations(entry,event_id)
    }
    return make_response(jsonify(payload),200)

@streaming.route('/V1/raw/latest/<event_id>')
def latest_entries_raw(event_id):
    payload = {
        "entries":[ e.json() for e in 
            Entry.query.filter(Entry.event_id==event_id,Entry.timestamp!=None).order_by(Entry.timestamp.desc()).limit(5)
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

# TODO rate limit the frames as they come in, so there are not big chunks of time with 100+ entries
@streaming.route('/stream/data',methods=["POST"])
def stream_in():
    print("VIDEO STREAM RECIEVED")
    # print(request.form.json)
    
    data_url = request.form.get("DataURL")
    event_id = request.form.get("EventID")
    device_id = request.form.get("DeviceID")

    # try:
    # get event
    event = Event.query.filter(Event.id==event_id).first()

    if event is None :
        return make_response("UNABLE TO SAVE ENTRY",200)

    # Process and save data
    img = stringToImage(data_url.split(",")[1])
    resp = save_event_record(img,device_id,event)
    print("MAde it to the returns statement")
    print("REsp: ",resp)
    return make_response("MID",200) 
    # except:
        

    return make_response("UNABLE TO SAVE ENTRY",200)

# @socketio.on('VideoStreamIn', namespace='/iris')
# def stream_in(data):
#     print("VIDEO STREAM RECIEVED")
#     print(data)
    
#     data_url = data["DataURL"]
#     event_id = data["EventID"]
#     device_id = data["DeviceID"]

#     # get event
#     event = Event.query.filter(Event.id==event_id).first()

#     if event is None :
#         emit('VideoStreamReceived', {'Valid': False}, namespace='/iris')
#     # Process and save data
#     img = stringToImage(data_url.split(",")[1])
#     save_event_record(img,device_id,event)
 
#     emit('VideoStreamReceived', {'Valid': True}, namespace='/iris')

@socketio.on('connect', namespace='/iris')
def test_connect():
    print("SOCKETIO CONNECTED")

def stringToImage(base64_string):
    imgdata = np.fromstring(base64.b64decode(base64_string), np.uint8)
    return cv2.imdecode(imgdata, cv2.IMREAD_COLOR)


def read_js_date(datestring):
    return datetime.datetime.strptime(datestring, "%a, %d %b %Y %H:%M:%S %Z")