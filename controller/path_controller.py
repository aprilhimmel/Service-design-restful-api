from model.repository.path_repo import PathRepo
pr = PathRepo()


def user_exists(user):
    pr.existing_user(user)
    return
