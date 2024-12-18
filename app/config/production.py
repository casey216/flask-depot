import os
from .default import DefaultConfig

class ProductionConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('PRODUCTION_DATABASE_URL', 'sqlite:///production.db')
    # Additional production-specific settings
