from app import app
from flask import Response, request
import json
import controller.users_controller as usc
import controller.apis_controller as ac


@app.route("/")
def index():
    return "Welcome"


@app.route('/metaapi/users', methods=['GET'])
def get_all_users():
    users = usc.get_all_users()
    return json.dumps(users), 200, {'Content-Type': 'application/json'}


@app.route('/metaapi/users', methods=['POST'])
def add_user():
    data_string = request.get_json()
    usc.add_user(data_string)
    return json.dumps({'Success': True}), 201, {'Content-Type': 'application/json'}


@app.route('/metaapi/users/<string:id>', methods=['GET'])
def get_user_by_id(id):
    user = usc.get_user_by_id(id)
    return json.dumps(user.to_dict()), 200, {'Content-Type': 'application/json'}


@app.route('/metaapi/users/<string:id>', methods=['DELETE'])
def delete_user_by_id(id):
    usc.delete_user(id)
    return json.dumps({'Success': True}), 200, {'Content-Type': 'application/json'}


@app.route('/metaapi/users/<string:id>', methods=['PUT'])
def put_user_by_id(id):
    request_data = request.get_json()
    usc.change_entire_user_info(id, request_data)
    return json.dumps({'Success': True}), 200, {'Content-Type': 'application/json'}


@app.route('/metaapi/users/<string:id>', methods=['PATCH'])
def patch_user(id):
    request_data = request.get_json()
    usc.change_fields(id, request_data)
    return json.dumps({'Success': True}), 201, {'Content-Type': 'application/json'}


# ALL API ROUTES

@app.route('/metaapi/users/<string:id>/apis', methods=['GET'])
def get_all_apis_for_user(id):
    apis = ac.get_all_apis(id)
    return json.dumps(apis), 200, {'Content-Type': 'application/json'}


@app.route('/metaapi/apis/<string:id>', methods=['GET'])
def get_api(id):
    pass


@app.route('/metaapi/users/<string:id>/apis/', methods=['POST'])
def add_api_to_user(id):
    data = request.get_json()
    ac.add_api(id, data)
    return json.dumps({'Success': True}), 201, {'Content-Type': 'application/json'}


@app.route('/metaapi/apis/<string:id>', methods=['DELETE'])
def delete_api(id):
    ac.delete_api(id)
    return json.dumps({'Success': True}), 200, {'Content-Type': 'application/json'}



# ROUTE FÖR ADRESSERING ENLIGT ANVÄNDAREN

#
# @app.route("/apis/<path:uri>", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
# def apis(uri):
#     parts = uri.split('/')
#     if len(parts) < 2:
#         return json.dumps({'error: url must contain at least username and api name'})
#     user = parts[0]
#     if not parts[0] == {user_name}# check against our users list
#     api = parts[1]
#     uri = parts[2:]
#     method = request.method
#     resp = {
#         'method': method,
#         'user': user,
#         'api': api,
#         "uri-parts": uri,
#     }
#     return json.dumps(resp)
