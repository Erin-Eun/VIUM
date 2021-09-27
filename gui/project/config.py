import os

BASE_DIR = os.path.dirname(__file__)

# Database Route
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'vium.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY="secretkey"