import sqlalchemy as sa
from sqlalchemy.orm import relationship
from model.db import db
import model.models.apis


class User(db.Model): # parent till apis
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    apis = relationship("Api")

    def to_dict(self):
        return {'user_id': self.id, 'username': self.username, 'password': self.password,
                'email': self.email, "apis": [api.to_dict() for api in self.apis]}


#db.create_all()
#db.session.commit()