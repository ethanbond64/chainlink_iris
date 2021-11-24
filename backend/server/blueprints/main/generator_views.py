from flask import json, render_template, Blueprint, make_response, jsonify, request
from server.blueprints.main.models import Event, Entry, Contract
from server.blueprints.main.contract_generator import ContractWriter
from flask_cors import CORS


generator = Blueprint('generator', __name__,template_folder='templates')
CORS(generator,origins="http://localhost:3000")


@generator.route('/generate/contract', methods=["POST"])
def generate_contract():

    env_json = request.form.get("env_json")
    event_id = request.form.get("entry_id")
    name = request.form.get("name")

    contract = Contract(event_id=event_id,env_json=env_json).save()

    contract.filename = ContractWriter(name,event_id,env_json).write()

    return make_response(jsonify({"Generated":False}),200)


@generator.route('/view/contract')
def view_contract():
    # TODO
    return "Text response will make up a sol file"


@generator.route('/deploy/contract')
def deploy_contract():
    # TODO
    return make_response(jsonify({"Deployed":False}),200)