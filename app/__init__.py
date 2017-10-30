from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

ADMINS = ['maria']

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config.from_object('config')
db = SQLAlchemy(app)

users = {
    'viktor': 'hello123',
    'yuriy': "bye123",
    'maria': "admin123"
}


@auth.get_password
def get_user_cred(username, password):
    if username in users and password == users.get(username):
        return True
    return False


from app import views, models
