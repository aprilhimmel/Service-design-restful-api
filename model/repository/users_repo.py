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

    def delete_user(self):
        pass


    def create_user(self, user):
        user = User(username=user['username'], password=user['password'], email=user['email'])
        session.add(user)
        session.commit()
        return

    def update_user(self, _id, new_username, new_password, new_email):
        update = session.query(User).filter(User.id == _id).first()
        update.username = new_username
        session.commit()
        update.password = new_password
        session.commit()
        update.email = new_email
        session.commit()
        return

    def change_username(self, id, username):
        session.query(User).filter(User.id == id).update({'username': username})
        session.commit()
        return

    def change_password(self, id, password):
        session.query(User).filter(User.id == id).update({'password': password})
        session.commit()
        return

    def change_email(self, id, email):
        session.query(User).filter(User.id == id).update({'email': email})
        session.commit()
        return

    def change_apis(self, id, apis):
        user.apis = apis
        # HUR UPPDATERA EN RELATION?
        session.commit()
        return
