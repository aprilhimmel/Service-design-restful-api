from sqlalchemy.orm import relationship
from model.db import db
import model.models.endpoints


class Api(db.Model):
    __tablename__ = "apis"
    id = db.Column(db.Integer, primary_key=True)
    api_name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = relationship("User") # ägaren/parent
    endpoints = relationship("Endpoint")

    def to_dict(self):
        return {'id': self.id, 'api_name': self.api_name, 'description': self.description,
                'user_id': self.user_id, 'endpoints': [endpoints.to_dict() for endpoints in self.endpoints]}

