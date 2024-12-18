import os
from .default import DefaultConfig

class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOPMENT_DATABASE_URL', 'sqlite:///development.db')
