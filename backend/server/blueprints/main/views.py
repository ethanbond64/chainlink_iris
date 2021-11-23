from flask import render_template, request, Blueprint, json, jsonify, make_response, render_template_string, Response
from server.blueprints.main.models import Event, Entry
from flask_cors import CORS
import datetime
from server.utils.extensions import socketio
from flask_socketio import emit
# from server.blueprints.main.camera import Camera
from server.blueprints.main.time_handler import img_to_bin
from PIL import Image
from io import StringIO, BytesIO 
import base64
import numpy as np
import re


# camera = Camera()

from server.blueprints.main.models import Event

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
                expiration=datetime.datetime.now()+datetime.timedelta(days=5))

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

@main.route('/timebox',methods=['GET'])
def view_timebox():
    return render_template('timebox.html')

# Video rts
@main.route('/',methods=['GET'])
def stream_video():
    return render_template('index.html')


# Sender

# def gen():
#     """Video streaming generator function."""

#     # app.logger.info("starting to generate frames!")
#     while True:
#         frame_data = camera.get_frame_data() #pil_image_to_base64(camera.get_frame())
#         yield frame_data


# @main.route('/video_info')
# def video_feed():
#     """Video streaming route. Put this in the src attribute of an img tag."""
#     return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


@socketio.on('VideoStreamIn', namespace='/iris')
def stream_in(data):
    
    data_url = data["DataURL"]
    event_id = data["EventID"]

    # get event
    event = Event.query.filter(Event.event_id==event_id).first()

    # Process and save data

    emit('VideoStreamReceived', {'Valid': True}, namespace='/iris')


@socketio.on('input image', namespace='/test')
def test_message(data_url):

    print("YOOOOOOO")
    # img = data_url
    # img_bytes = StringIO(data_url).getvalue()
    # print(type(img_bytes))
    # img = Image.open(img_bytes)
    img = stringToImage(data_url.split(",")[1])
    # jpg_original = decode_base64(bytes(data_url))
    # jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
    num = 0
    try:
        num = img_to_bin(img)
        print("Calculated Num: ",num)
    except:
        pass
    

    # print(len(img))
    # img = img.split(",")[1]
    # camera.enqueue_input(img)

    emit('out-image-event', {'image_data': num}, namespace='/test')
    #camera.enqueue_input(base64_to_pil_image(input))


@socketio.on('connect', namespace='/test')
def test_connect():
    print("YOOO CONNECT")
    # app.logger.info("client connected")


def stringToImage(base64_string):
    imgdata = base64.b64decode(base64_string)
    return  np.array(Image.open(BytesIO(imgdata)))