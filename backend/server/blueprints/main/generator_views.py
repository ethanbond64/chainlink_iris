from flask import json, render_template, Blueprint, make_response, jsonify, request
from server.blueprints.main.models import Event, Entry, Contract
from server.blueprints.main.contract_generator import ContractWriter
from flask_cors import CORS


generator = Blueprint('generator', __name__,template_folder='templates')
CORS(generator,origins="http://localhost:3000")

SOL_PATH = "backend/server/blueprints/main/generated_sol"

@generator.route('/generate/contract', methods=["POST"])
def generate_contract():

    env_json = request.form.get("env_json")
    event_id = request.form.get("entry_id")
    name = request.form.get("name")

    contract = Contract(event_id=event_id,env_json=env_json).save()

    contract.filename = ContractWriter(name,event_id,env_json).write()

    return make_response(jsonify({"Generated":False}),200)


@generator.route('/view/contract/<c_id>',methods=["GET"])
def view_contract(c_id):
    contract = Contract.query.filter(Contract.id==c_id).first()
    if contract is not None:
    
        fname = SOL_PATH+contract.filename
        sol = """ """

        try:
            with open(fname,"r") as file:
                sol = file.read()
            
            resp = make_response(sol, 200)
            resp.mimetype = "text/plain"

            return resp
        
        except:
            return make_response("Error finding file", 500)
    return make_response(jsonify({"Error":"Invalid contract id"}),200)


@generator.route('/deploy/contract')
def deploy_contract():
    # TODO
    return make_response(jsonify({"Deployed":False}),200)