from app import app
from flask import Response, request
import json
import controller.users_controller as usc
import controller.apis_controller as ac
import controller.path_controller as pc
import app.create_schemas as schema
import controller.endpoints_controller as ec


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


@app.route('/metaapi/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = usc.get_user_by_id(id)
    return json.dumps(user.to_dict()), 200, {'Content-Type': 'application/json'}


@app.route('/metaapi/users/<string:username>', methods=['GET'])
def get_user_by_name(username):
    user = usc.get_user_by_name(username)
    if not pc.user_exists(username):
        return json.dumps({'error': 'User does not exist'})
    else:
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


@app.route('/metaapi/users/<string:username>/apis/<string:apiid>', methods=['PUT'])
def change_api(username, apiid):
    data = request.get_json()
    ac.change_api(apiid, username, data)
    return json.dumps({'Success': True}), 200, {'Content-Type': 'application/json'}


@app.route('/metaapi/users/<string:id>/apis', methods=['PATCH'])
def change_api_field(id):
    return json.dumps({'Success': True}), 200, {'Content-Type': 'application/json'}


# ALL ENDPOINT ROUTES

@app.route('/metaapi/users/<string:id>/apis/<string:apiID>/endpoints', methods=['GET'])
def get_all_endpoints_for_api(id, apiID):
    endpoints = ec.get_all_endpoints(apiID)
    return json.dumps(endpoints), 200, {'Content-Type': 'application/json'}


@app.route('/metaapi/users/<string:id>/apis/<string:apiid>/endpoints/<string:end_id>', methods=['GET'])
def get_uri(id, apiid, end_id):
    endpoint = ec.get_endpoint_uri(end_id)
    return json.dumps(endpoint), 200, {'Content-Type': 'application/json'}


@app.route('/metaapi/users/<string:username>/apis/<string:apiname>', methods=['POST'])
def add_endpoint(username, apiname):
    data_string = request.get_json()
    ec.add_endpoint(apiname, data_string)
    return json.dumps({'Success': True}), 201, {'Content-Type': 'application/json'}


# ROUTE FÖR ADRESSERING ENLIGT ANVÄNDAREN
# metaapi/users/alice/awesomeapi/stuff
# http://127.0.0.1:5000/apis/alice/AwesomeAPI/dan

@app.route("/apis/<path:uri>", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def apis(uri):
    parts = uri.split('/')
    if len(parts) < 2:
        return json.dumps({'error: url must contain at least username and api name'})
    user = parts[0]
    if not pc.user_exists(user):
        return json.dumps({'error': 'User does not exist'})
    else:
        user_id = pc.check_user_id(user)
    api = parts[1]
    if not pc.api_exists(api, user_id):
        return json.dumps({'error': 'Api does not exist'})
    else:
        api_id = pc.check_api_id(api)
    uri = parts[2:]
    for u in uri:
        if not pc.endpoint_exists(u, api_id):
            return json.dumps({'error': 'Endpoint does not exist'})
        else:
            return
    # if post , create schema
    # if get , gå in och hämta i en databas
    # if put , ändra i databasen
    # if patach, ändra i databasen

    method = request.method
    if method == 'GET':
        pc.get_req()
    if method == 'POST':
        data = request.get_json()
        pc.post_req(data)
    if method == 'PUT':
        pass
    if method == 'PATCH':
        pass
    if method == 'DELETE':
        pass

    resp = {
        'method': method,
        'user': user,
        'api': api,
        "uri-parts": uri,
    }
    return json.dumps(resp)


def add_new_data():
    data = request.get_json()
    schema.create_schema_from_dict(data)


