from run import db
# from sqlalchemy.dialects.postgresql
from datetime import datetime

#   all users of the app (offline + online / all created accounts)
class Users(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    online_status = db.Column(db.Boolean())

    def __init__(self, user_id, username, first_name, last_name, online_status):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.online_status = online_status

    def __repr__(self):
        return f'<user_id {self.user_id} username {self.username} first_name {self.first_name} last_name {self.last_name} online_status {self.online_status}'

#TODO   probably need to make a list or dict of all the messages for each user
#       or they won't be able to load the messages properly and efficiently
#   messages between user and their friend(s), only 1 on 1 chat being implemented
class UserMessages(db.Model):
    __tablename__ = 'user_messages'
    
    user_id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    message = db.Column(db.String(100), nullable=False)
    #   other ids
    message_between = db.Column(db.Integer())
    message_date = db.Column(db.DateTime)

    def __init__(self, user_id, message, message_between, message_date):
        self.user_id = user_id
        self.message = message
        self.message_between = message_between
        self.message_date = message_date
    
    def __repr__(self):
        return f'<user_id {self.user_id} message {self.message} message_between {self.message_between} message_date {self.message_date}'

class LoginData(db.Model):
    __tablename__ = 'login_data'

    user_id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    access_token = db.Column(db.String(256), nullable=False)
    refresh_token = db.Column(db.String(256), nullable=False)
    
    def __init__(self, user_id, email, password, access_token, refresh_token):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.access_token = access_token
        self.refresh_token = refresh_token
    
    def __repr__(self):
        return f'<user_id {self.user_id} email {self.email} password {self.password} access_token {self.access_token} refresh_token {self.refresh_token}'
