import os
from .default import DefaultConfig

class TestingConfig(DefaultConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TESTING_DATABASE_URL', 'sqlite:///testing.db')
    WTF_CSRF_ENABLED = False
