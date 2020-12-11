import re

from model.repository.path_repo import PathRepo
pr = PathRepo()


def user_exists(user):
    if pr.existing_user(user):
        return True
    else:
        return False


def check_user_id(user):
    user_id = pr.check_user_id(user)
    return user_id


def api_exists(api, user_id):
    if pr.existing_api(api, user_id):
        return True
    else:
        return False


def check_api_id(api):
    api_id = pr.check_api_id(api)
    return api_id


def endpoint_exists(uri, api_id):
    if pr.existing_table(uri, api_id):
        return True
    else:
        return False

def get_req():
    pass


def post_req(data):
    pr.post_req(data)
    return

def put_req():
    pass

def patch_req():
    pass

def delete_req():
    pass