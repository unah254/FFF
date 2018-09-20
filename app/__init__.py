from flask import Flask
from flask_restful import  Api
from instance.config import app_config


from .api.v1.views import SingleOrder, Orders, Createmeal




def create_app(config_name):
    """
    Given a configuration name, loads the correct 
    configuration from the config.py
    :param config_name: The configuration name to load the configuration
    :return: The app to be initialized
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    

    api = Api(app)
    api.add_resource(SingleOrder, '/api/v1/orders/<int:id>')
    api.add_resource( Orders, '/api/v1/orders')
    api.add_resource( Createmeal, '/api/v1/orders')

        

    
    
    return app