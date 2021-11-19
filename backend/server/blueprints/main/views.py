from flask import render_template, request, Blueprint, json, jsonify, make_response, render_template_string, Response
from server.blueprints.main.models import Event, Entry
from flask_cors import CORS
import datetime
from server.utils.extensions import socketio
from flask_socketio import emit
from server.blueprints.main.camera import Camera, Makeup_artist

camera = Camera(Makeup_artist())

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

def gen():
    """Video streaming generator function."""

    # app.logger.info("starting to generate frames!")
    while True:
        frame = camera.get_frame() #pil_image_to_base64(camera.get_frame())
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@main.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


@socketio.on('input image', namespace='/test')
def test_message(input):
    print("YOOOOOOO")
    input = input.split(",")[1]
    camera.enqueue_input(input)
    image_data = input # Do your magical Image processing here!!
    #image_data = image_data.decode("utf-8")
    image_data = "data:image/jpeg;base64," + image_data
    print("OUTPUT " + image_data)
    emit('out-image-event', {'image_data': image_data}, namespace='/test')
    #camera.enqueue_input(base64_to_pil_image(input))


@socketio.on('connect', namespace='/test')
def test_connect():
    print("YOOO CONNECT")
    # app.logger.info("client connected")