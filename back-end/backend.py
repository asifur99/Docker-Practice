import os
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return 'Hello World!'

class Users(Resource):
    # methods go here
    def get(self):
        data = pd.read_csv('./user.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code

class Locations(Resource):
    # methods go here
    def get(self):
        data = pd.read_csv('./location.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code

api.add_resource(Users, '/users')  # '/users' is our entry point
api.add_resource(Locations, '/locations')  # '/locations' is our entry point

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port) # Run the flask app