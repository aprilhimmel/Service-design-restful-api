from flask import request
import re

from model.db import session


     # UNDER KONSTRUKTION
def create_schema_from_dict(data):
    schema = data['schema']

    fields = [key for key in schema.keys() if type(schema[key]) != list and key != 'schema_name']
    schema_name = schema['schema_name']
    types = []
    for field in fields:
        type_data = schema[field]
        if type_data == 'primary_key':
            types.append('integer primary key auto_increment')
        elif type_data == 'inner_schema':
            field2 = [key for key in type_data.keys() if key != 'schema_name']

        elif type_data == 'string' and type_data != r'[[:digit:]]':
            types.append('varchar')
        elif type_data.startswith("string"):
            size = re.findall(r'\(\d+\)', type_data)[0]
            types.append(f'varchar{size}')
        elif type_data.startswith('int'):
            types.append('integer')
        elif type_data.startswith('text'):
            types.append('text')
    field_row_creator(fields, types, schema_name)


def field_row_creator(fields, types, schema_name):
    field_rows = ','.join(fields[i] + ' ' + types[i] for i in range(len(types)))
    table_creator(schema_name, field_rows)


def table_creator(schema_name, field_rows):
    sql_str = f"CREATE TABLE {schema_name} ({field_rows})"
    print(sql_str)
    session.engine.execute(sql_str)
    #db.engine.execute(sql_str)


    # need to have check if this uri already exists in users table,
    # need to add only if not exists
    # need to add foreign key
