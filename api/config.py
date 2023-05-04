import os 

class Config:
    SECRET_KEY = "0980551df15adb62feb88da4c613a379"
    CORS_HEADERS = 'Content-Type'

    @staticmethod
    def init_app(app):
        pass 


class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    Testing = True

class ProductionConfig(Config):
    production = True

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}