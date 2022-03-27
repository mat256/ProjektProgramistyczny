from flask import Flask
from flask_restful import Resource, Api
from modules.dane import data_new
#import modules.movies

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Links(Resource):
    def get(self):
        return data_new('modules/links.csv')


api.add_resource(HelloWorld, '/')
api.add_resource(Links, '/links')

if __name__ == '__main__':
    app.run(debug=True)