import re

from model.models.apis import Api
from model.models.user import User
from model.models.endpoints import Endpoint
from app.create_schemas import create_schema_from_dict


class PathRepo:
    def existing_user(self, usernam):
        user = User.query.filter_by(username=usernam).first()
        if user is None:
            return False
        elif user.username == usernam:
            return True
        else:
            return False

    def check_user_id(self, user):
        user = User.query.filter_by(username=user).first()
        user_id = user.id
        return user_id

    def existing_api(self, apin, user_id):
        api = Api.query.filter_by(api_name=apin).first()
        if api is None:
            return False
        elif api.api_name == apin and api.user_id == user_id:
            return True
        else:
            return False

    def check_api_id(self, api):
        api = Api.query.filter_by(api_name=api).first()
        api_id = api.id
        return api_id

    def existing_table(self, uri, apisid):
        endpoints = Endpoint.query.filter_by(uri=uri).first()
        if endpoints is None:
            return False
        elif endpoints.uri == uri and endpoints.api_id == apisid:
            return True
        else:
            return False


    def post_req(self, data):
        _uri = data['schema']['schema_name']
        endpoints = Endpoint.query.filter_by(uri=_uri).first()
        if endpoints is None:
            create_schema_from_dict(data)
            return False
        else:
            # om tabellen finns, fyll i kolumner enligt värdena nedan
            schema = data['schema']
            fields = [key for key in schema.keys() if type(schema[key]) != list and key != 'schema_name']
            values = [v for v in schema.values()]
            print(values)
            # schema_name = schema['schema_name']
            #
            # columns = Endpoint.__table__.columns.keys()
            # for i in columns:
            #     if i in values:
            #
            #     schema_name.k
            #     update
            #     CUSTOMERS
            #     set
            #     ORDER_PRICE = 4.7
            #     where
            #     FIRST_NAME = 'The' and LAST_NAME = 'Dude'
            # for field in fields:
            #     value_data = schema[field]
            #     endpoints.
            #     if valu == 'primary_key':
            #         types.append('integer primary key')
            #     elif type_data.startswith("string"):
            #         size = re.findall(r'\(\d+\)', type_data)[0]
            #         types.append(f'varchar{size}')
            #     elif type_data.startswith('int'):
            #         types.append('integer')
            #     elif type_data.startswith('text'):
            #         types.append('text')
            #
            # field_rows = ', '.join(fields[i] + ' ' + types[i] for i in range(len(types)))
            # print(field_rows)
            #
            # sql_str = f"INSERT INTO {schema_name} VALUES ({field_rows})"
            # print(sql_str)
