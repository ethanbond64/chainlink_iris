from flask import render_template, request, Blueprint, json, jsonify, make_response, render_template_string
from flask_cors import CORS
from requests import get
import os

from server.blueprints.main.models import Event

main = Blueprint('main', __name__)

CORS(main,origins="http://localhost:3000")


# GET ENDPOINTS
@main.route('/test',methods=['GET'])
def get_test():
    return make_response(jsonify({"Test":True}))

# @chia.route('/allcoins', methods=['GET'])
# def get_all_coins():

#     coins = Coin.query.order_by(Coin.created_on.desc()).all()
#     resp = {"coins":[coin.json() for coin in coins]}

#     return make_response(jsonify(resp),200)

# @chia.route('/coin/name/<name>', methods=['GET'])
# def get_coin_by_name(name):

#     coin = Coin.query.filter(Coin.name==name).first()
#     resp = {"data":{}}

#     if coin is not None:

#         resp["data"] = coin.json()
        
#         return make_response(jsonify(resp),200)

#     return make_response(jsonify(resp),400)

# @chia.route('/puzzlehash/id/<id>')
# def get_puzzlehash_by_id(id):
    
#     coin = Coin.query.filter(Coin.id==id).first()

#     if coin is not None:
        
#         resp = {"puzzlehash":coin.puzzlehash}

#         return make_response(resp, 200)
    
#     return make_response({}, 400)

# @chia.route('/allspends', methods=['GET'])
# def get_all_spends():

#     spends = Spend.query.all()
#     resp = {"spends":[spend.json() for spend in spends]}

#     return make_response(jsonify(resp),200)


# # DELETE ENDPOINTS

# @chia.route('/delete/coin',methods=['POST'])
# def delete_coin():

#     resp = {"success":False}
    
#     if request.form.get("id") is not None:

#         coin = Coin.query.filter(Coin.id == int(request.form.get("id"))).first()
        
#         if coin is not None:

#             coin.delete()
#             resp = {"Success":True,"name":coin.name}

#             return make_response(jsonify(resp),200)

#     return make_response(jsonify(resp),400)

# @chia.route('/delete/spend',methods=['POST'])
# def delete_spend():

#     resp = {"success":False}
    
#     if request.form.get("id") is not None:

#         spend = Spend.query.filter(Spend.id == int(request.form.get("id"))).first()
        
#         if spend is not None:

#             spend.delete()
#             resp = {"Success":True,"name":spend.name}

#             return make_response(jsonify(resp),200)

#     return make_response(jsonify(resp),400)

# # BUILD ENDPOINTS

# @chia.route('/build/coin/',methods=['POST'])
# def build_coin():
#     resp = {}

#     if request.form.get("name") is not None:

#         # TODO Add validations on the puzzlejson
#         print(json.loads(request.form.get("puzzlejson")))
#         new_coin = Coin(name=request.form.get("name"))
#         new_coin.save_puzzlejson(json.loads(request.form.get("puzzlejson")))

#         writer = ChialispWriter(new_coin.puzzlejson,new_coin.name)
#         fname = writer.writeAll()

#         new_coin.filename = fname
#         new_coin.puzzlehash = "PUZZLEHASH GENERATION IN PROGRESS"
#         new_coin.save()

#         # Kick off async task to build hash the puzzle code
#         from server.blueprints.main.tasks import predeploy_coin_async

#         predeploy_coin_async.delay(new_coin.id)
#         resp = new_coin.json()

#         return make_response(jsonify(resp),200)

#     return make_response(jsonify(resp),400)

# @chia.route('/build/spend',methods=['POST'])
# def build_spend_bundle():

#     resp = {"success":False}
    
#     if request.form.get("data") is not None:
        
#         spend_name = request.form.get("name")
#         data = json.loads(request.form.get("data"))

#         coin_ids = data.get("coins")
#         coins = Coin.query.filter(Coin.id.in_(coin_ids)).all()

#         solns = data.get("solutions")

#         if spend_name == None or coin_ids == [] or None in coin_ids or None in solns:
#             resp["error"] = "Missing Fields Required for Spend Bundle"
#             return make_response(resp, 400)

#         try:
#             fname,agg_sig =  SpendWriter(coins,solns,spend_name).build_spend_bundle()

#             # TODO create spendbundle record
#             spend = Spend(name=spend_name,filename=fname,agg_sig=agg_sig)
#             spend.save()

#             resp = {"success":"True","fname":fname,"aggsig":agg_sig}
#             return make_response(resp,200)
        
#         except Exception as e:
#             resp["error"] = e
#             return make_response(resp,400)

#     return make_response(resp, 400)


# # DEPLOY ENDPOINTS

# @chia.route('/deploycoin',methods=['POST'])
# def deploy_coin():
#     print("Recieved")

#     resp = {"success":False}
#     if request.form.get("id") is not None:

#         coin = Coin.query.filter(Coin.id==request.form.get("id")).first()
        
#         if coin is not None:
            
#             coin.netaddress = ChialispDeployer.deploy(coin.puzzlehash)
#             coin.save()

#             resp = {"netaddress":net_address,"Success":True}

#             return make_response(jsonify(resp),200)

#     return make_response(jsonify(resp),400)


# # READ/TEXT ENDPOINTS

# @chia.route('/chialisp/id/<id>')
# def view_chialisp_by_id(id):
    
#     coin = Coin.query.filter(Coin.id==id).first()

#     if coin is not None:
    
#         fname = CLSP_PATH+coin.filename
#         clsp = """ """

#         try:
#             with open(fname,"r") as file:
#                 clsp = file.read()
            
#             header = coin.filename+"\n\n\n"
#             resp = make_response(header+clsp, 200)
#             resp.mimetype = "text/plain"

#             return resp
        
#         except:
#             return make_response("Error finding file", 500)

#     return make_response("Could not find coin", 400)

# @chia.route('/spendjson/id/<id>')
# def view_spend_json_by_id(id):
    
#     spend = Spend.query.filter(Spend.id==id).first()

#     if spend is not None:
    
#         fname = JSON_PATH+spend.filename
#         json_contents = """ """

#         try:
#             with open(fname,"r") as file:
#                 json_contents = json.loads(file.read())
            
#             return make_response(jsonify(json_contents), 200)
        
#         except:
#             return make_response("Error finding file", 500)

#     return make_response("Could not find spend", 400)




# def proxy(host, path):
#     print(f"{host}{path}")
#     response = get(f"{host}{path}")
#     excluded_headers = [
#         "content-encoding",
#         "content-length",
#         "transfer-encoding",
#         "connection",
#     ]
#     headers = {
#         name: value
#         for name, value in response.raw.headers.items()
#         if name.lower() not in excluded_headers
#     }
#     return (response.content, response.status_code, headers)

# WEBPACK_DEV_SERVER_HOST = "http://chianocode_frontend_1:3000/"

# # @journal.route("/sockjs-<node>")
# @chia.route("/hotreload/")
# @chia.route("/hotreload/<path:path>")
# def hot_reload(path='',node=None):
    
#     # if path == '/':
#     #     return render_template_string(index_string)
#     # print("FUCK")
#     # print(path)
#     # return "hey"
#     # if node == 'node':
#     #     return proxy("http://innerly_client_1:3000","/sockjs-node")


#     # if path == 'static/js/vendors~main.chunk.js':
#     #     print('FIXXXXINNN ITTT')
#     #     resp =  proxy(WEBPACK_DEV_SERVER_HOST, "hotreload/"+path)
#     #     resp = (resp[0].decode("utf-8").replace('port: undefined','port: 3000'),resp[1],resp[2])
#     #     # print(resp[0])
#     #     return resp
    

#     if path == '':
#         bytestr = proxy(WEBPACK_DEV_SERVER_HOST, "hotreload/")[0]
#         # print(bytestr)
#         print(type(bytestr))
#         return render_template_string(bytestr.decode("utf-8"))

#     return proxy(WEBPACK_DEV_SERVER_HOST, "hotreload/"+path)
