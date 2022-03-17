import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'MMOQLDpZOgsF1sFjx4nitkbheSNzPqGIt1+X3h1vPPQ='
    SQLALCHEMY_DATABASE_URI = os.environ['postgresql+psycopg2://bruno:dollar@localhost/db_test']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
