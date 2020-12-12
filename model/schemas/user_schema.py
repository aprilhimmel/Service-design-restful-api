# from model.db import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from model.models.user import User


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True


user_schema = UserSchema
users_schema = UserSchema (many=True)



