from model.repository.apis_repo import ApisRepo
ar = ApisRepo()


def get_all_apis(user_id):
    apis = ar.get_all_apis()
    apis = [api.to_dict() for api in apis]
    return apis


def api_by_id(id):
    api = ar.add_api(id)
    return api


def add_api(id, data):
    ar.add_api(id, data)
    pass
