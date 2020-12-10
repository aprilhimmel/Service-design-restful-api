from model.repository.apis_repo import ApisRepo
ar = ApisRepo()


def get_all_apis(user_id):
    apis = ar.get_all_apis(user_id)
    apis = [api.to_dict() for api in apis]
    return apis


def api_by_id(id):
    api = ar.add_api(id)
    return api


def add_api(id, data):
    ar.add_api(id, data)
    pass


def change_api(id, username, data):
    new_name = data['api_name']
    new_description = data['description']
    ar.update_api(id, username, new_name, new_description)
    return


def change_api_name():
    pass


def change_api_description():
    pass


def delete_api(id):
    ar.delete_api(id)
    return
