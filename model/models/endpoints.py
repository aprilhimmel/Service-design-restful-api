from sqlalchemy.orm import relationship
from model.db import db, to_dict
import model.models.apis


@to_dict(['id', 'uri', 'api_id'])
class Endpoint(db.Model):  # child till apis
    __tablename__ = "endpoints"
    id = db.Column(db.Integer, primary_key=True)
    uri = db.Column(db.String(100), nullable=False)
    api_id = db.Column(db.Integer, db.ForeignKey("apis.id"))
    apis = relationship("Api") # api is parent to endpoint

    def to_dict(self):
        return {'id': self.id, 'uri': self.uri, 'api_id': self.api_id,
                'apis': self.apis}
