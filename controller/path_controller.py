from model.repository.path_repo import PathRepo
pr = PathRepo()


def user_exists(user):
    if pr.existing_user(user):
        return True
    else:
        return False
