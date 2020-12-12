import os
from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import app

basedir = os.path.abspath(os.path.dirname(__file__))
print(os.path.join(basedir, 'db.sqlite'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init db
db = SQLAlchemy(app)
# init ma
# ma = Marshmallow(app)

engine = create_engine('sqlite:///' + os.path.join(basedir, 'db.sqlite'))
Session = sessionmaker(bind=engine)
session = Session()


def to_dict(attributes):
    def wrapper(cls):
        def to_dict(self):
            for a in attributes:
                if a not in self.__dict__:
                    raise ValueError(f"{a} not a member of the object {self}")
            return {attr: self.__dict__[attr] for attr in attributes}
        cls.to_dict = to_dict
        return cls
    return wrapper

# import sqlite3
#
#
# def add_column(database_name, table_name, column_name, data_type):
#
#   connection = sqlite3.connect(database_name)
#   cursor = connection.cursor()
#
#   if data_type == "Integer":
#     data_type_formatted = "INTEGER"
#   elif data_type == "String":
#     data_type_formatted = "VARCHAR(100)"
#
#   base_command = ("ALTER TABLE '{table_name}' ADD column '{column_name}' '{data_type}'")
#   sql_command = base_command.format(table_name=table_name, column_name=column_name, data_type=data_type_formatted)
#
#   cursor.execute(sql_command)
#   connection.commit()
#   connection.close()
