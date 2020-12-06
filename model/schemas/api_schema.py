from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from model.models.apis import Api


class ApiSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Api
        include_relationships = True
        load_instance = True  # "Optional: deserialize to model instances"

