from app import app
from flask import Response, request
import json
import controller.users_controller as usc
import controller.apis_controller as ac


@app.route("/")
def index():
    return "Welcome"


@app.route('/users', methods=['GET'])
def get_all_users():
    users = usc.get_all_users()
    return Response(json.dumps(users), mimetype='application/json')


@app.route('/users', methods=['POST'])
def add_user():
    data_string = request.get_json()
    usc.add_user(data_string)
    return json.dumps({'status': 'Success'}), 201, {'ContentType': 'application/json'}


@app.route('/users/<string:id>', methods=['GET'])
def get_user_by_id(id):
    user = usc.get_user_by_id(id)
    return json.dumps(user.to_dict()), 200, {'ContentType': 'application/json'}


@app.route('/users/<string:id>', methods=['DELETE'])
def delete_user_by_id(id):
    usc.delete_user(id)
    return json.dumps({'status': 'User deleted'}), 200, {'ContentType': 'application/json'}


@app.route('/users/<string:id>', methods=['PUT'])
def put_user_by_id(id):
    request_data = request.get_json()
    usc.change_entire_user_info(id, request_data)
    return json.dumps({"status": "Complete user update performed"}), 204, {'ContentType': 'application/json'}


@app.route('/users/<string:id>', methods=['PATCH'])
def patch_user(id):
    request_data = request.get_json()
    usc.change_fields(id, request_data)
    pass


# ALL API ROUTES

@app.route('/users/<string:id>/apis', methods=['GET'])
def get_all_apis_for_user(id):
    apis = ac.get_all_apis(id)
    return Response(json.dumps(apis), mimetype='application/json')


@app.route('/apis/<string:id>', methods=['GET'])
def get_api(id):
    pass


@app.route('/users/<string:id>/apis/', methods=['POST'])
def add_api_to_user(id):
    data = request.get_json()
    ac.add_api(id, data)
    return json.dumps({'Success': True}), 201, {'ContentType': 'application/json'}
