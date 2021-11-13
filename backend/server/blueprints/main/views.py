from flask import render_template, request, Blueprint, json, jsonify, make_response, render_template_string
from flask_cors import CORS
from requests import get
import datetime
import os

from server.blueprints.main.models import Event

main = Blueprint('main', __name__)

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
def create_event():
    resp = {"success":False}
    if request.form.get("name") is not None:
        event = Event(
                name=request.form.get("name"),
                expiration=datetime.datetime.now()+datetime.timedelta(days=5))

        event.save()
        

        resp['success'] = True
    return make_response(jsonify(resp),200)