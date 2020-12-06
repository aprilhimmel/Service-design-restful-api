import json

from model.db import session
from model.models.user import User
from model.schemas.user_schema import UserSchema
from flask import jsonify


class UsersRepo:
    def get_all_users(self):
        users = User.query.all()
        user_schema = UserSchema()
        user_schema.dump(User.query.all())
        return users

    def get_user_by_id(self, id):
        user = User.query.get(id)
        return user

    def create_user(self, user):
        user = User(username=user['username'], password=user['password'], email=user['email'])
        session.add(user)
        session.commit()
        return

    def changed_user(self, _id, new_user):
        old_user_info = User.query.get(_id)
        session.delete(old_user_info)
        new_user = User(id=new_user['id'], username=new_user['username'], password=new_user['password'], email=new_user['email'])  #  , apis=new_user['apis'])
        session.add(new_user)
        session.commit()
        return

    def change_username(self, id, username):
        user = User.query.get(id)
        user.username = username
        session.commit()
        return

    def change_password(self, id, password):
        user = User.query.get(id)
        user.password = password
        session.commit()
        return

    def change_email(self, id, email):
        user = User.query.get(id)
        user.email = email
        session.commit()
        return

    def change_apis(self, id, apis):
        user.apis = apis
        # HUR UPPDATERA EN RELATION?
        session.commit()
        return