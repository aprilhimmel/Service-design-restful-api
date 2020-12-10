from flask import json

from model.repository.users_repo import UsersRepo
from model.models.user import User

ur = UsersRepo()


def get_all_users():
    users = ur.get_all_users()
    users = [user.to_dict() for user in users]
    return users


def get_user_by_id(id):
    user = ur.get_user_by_id(id)
    return user


def add_user(data):
    ur.create_user(data)
    return


def delete_user(id):
    ur.delete_user(id)
    return


def change_entire_user_info(id, new_user_data):
    new_username = new_user_data['username']
    new_password = new_user_data['password']
    new_email = new_user_data['email']
    ur.update_user(id, new_username, new_password, new_email)
    return


def change_fields(id, request_data):
    if "username" in request_data:
        username = request_data['username']
        ur.change_username(id, username)

    if "password" in request_data:
        password = request_data['password']
        ur.change_password(id, password)

    if "email" in request_data:
        email = request_data['email']
        ur.change_email(id, email)
        return
    return

