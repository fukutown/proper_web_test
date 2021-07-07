import os

class BaseConfig(object):
    pass

class ProductionConfig(BaseConfig):
    pass

class DevelopmentConfig(BaseConfig):
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True

class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False

config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
