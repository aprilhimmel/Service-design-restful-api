from model.db import session
from model.models.apis import Api
from model.models.user import User
from model.schemas.api_schema import ApiSchema


class ApisRepo:
    def get_all_apis(self, id):
        apis = Api.query.filter(Api.user_id == id).all()
        api_schema = ApiSchema(many=True)
        api_schema.dump(Api.query.all())
        return apis

    def get_api(self, id):
        api = Api.query.get(id)
        return api

    def add_api(self, id, data):
        api = Api(api_name=data['api_name'], description=data['description'], user_id=id)
        session.add(api)
        session.commit()
        return

    def update_api(self, id, username, name, description):
        user = User.query.filter_by(username=username).first()
        if user is None:
            return  # {'error': 'The user does not exist'}, hur????
        elif user.username == username:
            update = session.query(Api).filter(Api.id == id).first()
            update.api_name = name
            session.commit()
            update.description = description
            session.commit()
            return

    def change_field(self, id, data):
        pass

    def delete_api(self, id):
        api = session.query(Api).get(id)
        session.delete(api)
        session.commit()
        return
