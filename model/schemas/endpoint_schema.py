from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from model.models.endpoints import Endpoint


class EndpointSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Endpoint
        include_relationships = True
        load_instance = True  # "Optional: deserialize to model instances"

