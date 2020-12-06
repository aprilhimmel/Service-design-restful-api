from model.db import session
from model.models.endpoints import Endpoint
from model.schemas.endpoint_schema import EndpointSchema
from model.models.apis import Api


class EndpointRepo:
    def get_all_endpoints(self, id):
        for a, e in session.query(Api, Endpoint).filter(Api.id == Endpoint.api_id).all():
            print("Api name: {} Invoice No: {} Amount: {}".format(a.api_name, e.api_name, e.endpoints))
        endpoints = Endpoint.query.all()
        endp_schema = EndpointSchema()
        endp_schema.dump(Endpoint.query.all())
        return endpoints

    def get_endpoint_uri(self, id):
        endpoint = Endpoint.query.get(id)
        end = endpoint.uri
        return end

    def add_endpoint(self, id, data):
        endp = Endpoint(uri=data['uri'], api_id=id)
        session.add(endp)
        session.commit()
        return

    def change_endpoint(self, id, data):
        pass
