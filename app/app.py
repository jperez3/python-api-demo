from flask import Flask
from flask_restful import Api, Resource, reqparse

### Initializing
app = Flask(__name__)
api = Api(app)

# @app.route('/')
# def index():
#   return 'Server Works!'
  
# @app.route('/greet')
# def say_hello():
#   return 'Hello from Server'

class Something(Resource):
    def get(self):
        return {'something':'test12345'}

    def post(self):
        json_post = request.get_json()
        return {'user provided': json_post}, 201  


api.add_resource(Something, '/')


if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')