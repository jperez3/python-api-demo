from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps


e = create_engine('sqlite:///app.db')

app = Flask(__name__)
api = Api(app)

class Alive(Resource):
    def get(self):
        return {'this':'is alive'}

class Groups_Meta(Resource):
    def get(self):
        #Connect to databse
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select GroupName,Groupcode from test_tbl")
        return {'groups': [i[0] for i in query.cursor.fetchall()]}

 
# api.add_resource(Departmental_Salary, '/dept/<string:department_name>')
api.add_resource(Alive, '/')
api.add_resource(Groups_Meta, '/groups')

if __name__ == '__main__':
     app.run(debug=True,host='0.0.0.0',port=5000)