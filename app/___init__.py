from flask import Flask
from flask_restful import Api

import config


def create_app(config_name):
    """
    Given a configuration name, loads the correct 
    configuration from the config.py
    :param config_name: The configuration name to load the configuration
    :return: The app to be initialized
    """

    app = Flask(__name__) 
    api = Api(app)

    app.config.from_object('config')
    

    return app