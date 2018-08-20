from flask import Flask
from flask_restful import Api
from api.resources import PhoneBookResource 

def create_app(env="dev"):
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(
        PhoneBookResource,
        '/api/v1/phonebook'
    )

    return app
