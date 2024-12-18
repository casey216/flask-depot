from .default import DefaultConfig
from .development import DevelopmentConfig
from .production import ProductionConfig
from .testing import TestingConfig

config = {
    'default': DefaultConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
