import os

baseddir = os.path.abspath(os.path.dirname(__file__))
TEAM_NAME = os.environ['TEAM_NAME']

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'devtest123'
    JSON_SORT_KEYS = False

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEBUG = True
    DEVELOPMENT = True

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    TESTING = True