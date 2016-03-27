import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'admin123'
OPENID_PROVIDERS = [
    {'name': 'viktor', 'password': 'viktor'},
    # {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    # {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    # {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    # {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'medcab.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
