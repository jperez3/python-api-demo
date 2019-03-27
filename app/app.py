from flask import flask
from flask_restful import Api, Resource, reqparse

### Initializing
app = Flask(__name__)
api = Api(app)
