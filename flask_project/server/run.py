from flask import Flask
# from api.ping_handler import ping_handler
# from api.home_handler import home_handler

# app.register_blueprint(home_handler)
# app.register_blueprint(ping_handler)

from flask_sqlalchemy import SQLAlchemy
#TODO   find out if useful
from flask_restful import Api
import psycopg2
import os

app = Flask(__name__)

#   setup global variables for app and db from .env
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODICIATIONS'] = False
db_type = os.environ['DATABASE_URI']
db_username = os.environ['DATABASE_USERNAME']
db_password = os.environ['DATABASE_PASSWORD']
db_host = os.environ['DATABASE_HOST']
db_port = os.environ['DATABASE_PORT']
db_name = os.environ['DATABASE_NAME']
app.config['SQLALCHEMY_DATABASE_URI'] = '{db_type}{db_user}:{db_pw}@{host}:{port}/{db_name}'.format(
    db_type=db_type, db_user=db_username, db_pw=db_password, host=db_host, port=db_port, db_name=db_name
)
print(app.config['SQLALCHEMY_DATABASE_URI'])
#   init sqlalchemy
db = SQLAlchemy(app)
api = Api(app)
#   secret key
app.secret_key = os.environ['APP_SECRET_KEY']

import views, models, resources
#migrate = Migrate(app, db)

#   check if db exists from cursor connection
#   create the db if it doesn't exist
connection = psycopg2.connect(f"user={os.environ['DATABASE_USERNAME']} password={os.environ['DATABASE_PASSWORD']}")
#   autocommit is needed because create db cannot run inside a transaction
connection.autocommit = True
cursor = connection.cursor()
cursor.execute("SELECT datname FROM pg_catalog.pg_database WHERE datname = 'pg_test_db_123'")
db_check = cursor.fetchone()
print(f'db_check {db_check}')
if not db_check:
    cursor.execute('CREATE DATABASE pg_test_db_123')

#db.init_app(app)
#   create tables for db
db.create_all()

api.add_resource(resources.UserRegistration, '/registration')

if __name__ == '__main__':
    print(os.environ['DATABASE_URL'])
    print(os.environ['SQLALCHEMY_DATABASE_URI'])
    app.run()