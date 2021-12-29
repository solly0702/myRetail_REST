import os
from flask import Flask
from dotenv import dotenv_values
from settings import ProdConfig, TestConfig, DevConfig
from api import bp


def configure_app(app):
    config = dotenv_values(".flask_env")

    if config["ENV"] == "production":
        CONFIG = ProdConfig
    elif config["ENV"] == "test":
        CONFIG = TestConfig
    else:
        CONFIG = DevConfig

    app.config.from_object(CONFIG)


def initialize_app(app):
    configure_app(app)
    register_blueprints(app)


def register_blueprints(app):
    app.register_blueprint(bp)


def create_app():
    app = Flask(__name__)
    initialize_app(app)
    return app
