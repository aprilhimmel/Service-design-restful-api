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
