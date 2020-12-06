from flask import json

from model.repository.users_repo import UsersRepo

gr = UsersRepo()


def get_all_users():
    users = gr.get_all_users()
    users = [user.to_dict() for user in users]
    return users


def get_user_by_id(id):
    user = gr.get_user_by_id(id)
    return user


def add_user(data):
    gr.create_user(data)
    return


def change_entire_user_info(id, new_user_data):
    new_user = (id, new_user_data['username'], new_user_data['password'], new_user_data['email'], new_user_data['apis'])
    gr.changed_user(id, new_user)
    return


def change_fields(id, request_data):
    if "username" in request_data:
        username = request_data['username']
        gr.change_username(id, username)
        return

    if "password" in request_data:
        password = request_data['password']
        gr.change_password(id, password)
        return

    if "email" in request_data:
        email = request_data['email']
        gr.change_email(id, email)
        return

    if "apis" in request_data:
        apis = request_data['apis']
        gr.change_apis(id, apis)
        return
    return

def delete_user(id):
    pass