from model.db import session
from model.models.apis import Api
from model.models.user import User
from model.schemas.api_schema import ApiSchema


class ApisRepo:
    def get_all_apis(self, id):
        for u, a in session.query(User, Api).filter(User.id == Api.user_id).all():
            print("ID: {} Username: {} Apis: {} Number of endpoints: {}".format(u.id, u.name, a.api_name, a.endpoints))
        apis = Api.query.all()
        api_schema = ApiSchema()
        api_schema.dump(Api.query.all())
        return apis

    def get_api(self, id):
        api = Api.query.get(id)
        return api

    def add_api(self, id, data):
#        user = User.query.get(id)
#        user.apis.append(ap)
#        session.commit()
        api = Api(api_name=data['api_name'], description=data['description'], user_id=id)
        session.add(api)
        session.commit()
        return

    def change_api(self, id, data):
        pass
