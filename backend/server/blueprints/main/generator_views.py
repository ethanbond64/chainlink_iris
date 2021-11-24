from flask import json, render_template, Blueprint, make_response, jsonify
from server.blueprints.main.models import Event, Entry
from flask_cors import CORS


generator = Blueprint('generator', __name__,template_folder='templates')
CORS(generator,origins="http://localhost:3000")


@generator.route('/generate/contract')
def generate_contract():
    # TODO
    return make_response(jsonify({"Generated":False}),200)


@generator.route('/view/contract')
def view_contract():
    # TODO
    return "Text response will make up a sol file"


@generator.route('/deploy/contract')
def deploy_contract():
    # TODO
    return make_response(jsonify({"Deployed":False}),200)