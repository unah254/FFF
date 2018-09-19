from flask import Flask
from flask_restful import  Api
# from flask_api import FlaskAPI
from instance.config import app_config

from orders import Orders



def create_app(config_name):
    """
    Given a configuration name, loads the correct 
    configuration from the config.py
    :param config_name: The configuration name to load the configuration
    :return: The app to be initialized
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    api = Api(app)

        
    api.add_resource(Orders, '/api/v1/orders')



    return app