import os

class DefaultConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CONTINUUM_AUTO_VERSION = True
