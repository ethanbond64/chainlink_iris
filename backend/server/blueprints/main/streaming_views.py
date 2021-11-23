from flask import render_template
from server.blueprints.main.models import Event
from server.utils.extensions import socketio
from flask_socketio import emit
from server.blueprints.main.views import main
from server.blueprints.main.time_handler import img_to_bin
from server.blueprints.main.data_manager import save_event_record

from PIL import Image
from io import StringIO, BytesIO 
import base64
import numpy as np

# Time authenticator route
@main.route('/timebox',methods=['GET'])
def view_timebox():
    return render_template('timebox.html')

# Video frame route
@main.route('/',methods=['GET'])
def stream_video():
    return render_template('index.html')


@socketio.on('VideoStreamIn', namespace='/iris')
def stream_in(data):
    
    data_url = data["DataURL"]
    event_id = data["EventID"]

    # get event
    event = Event.query.filter(Event.event_id==event_id).first()

    # Process and save data
    img = stringToImage(data_url.split(",")[1])
    save_event_record(img,event)

    emit('VideoStreamReceived', {'Valid': True}, namespace='/iris')

@socketio.on('connect', namespace='/iris')
def test_connect():
    print("SOCKETIO CONNECTED")



# Old routes
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
    return np.array(Image.open(BytesIO(imgdata)))