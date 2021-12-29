import os
from dotenv import dotenv_values


class BaseConfig(object):
    HOST = "0.0.0.0"
    PORT = 3003
    SECRET_KEY = dotenv_values(".flask_env")["SECRET_KEY"]


class ProdConfig(BaseConfig):
    ENV = "production"
    FLASK_DEBUG = False


class TestConfig(BaseConfig):
    ENV = "test"
    TESTING = True
    FLASK_DEBUG = False


class DevConfig(BaseConfig):
    ENV = "development"
    FLASK_DEBUG = True
