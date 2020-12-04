from sqlalchemy.orm import relationship
from model.db import db
import model.models.apis


class Endpoint(db.Model):  # child till apis
    __tablename__ = "endpoints"
    id = db.Column(db.Integer, primary_key=True)
    uri = db.Column(db.String(100), nullable=False)
    api_id = db.Column(db.Integer, db.ForeignKey("apis.id"))
    apis = relationship("Api")

    def to_dict(self):
        return {'id': self.id, 'uri': self.uri, 'api_id': self.api_id,
                'apis': [api.to_dict() for api in self.apis]}
