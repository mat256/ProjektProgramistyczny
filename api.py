from flask import Flask, request
from flask_restful import Resource, Api
from flasgger import LazyString
from flasgger import Swagger, LazyJSONEncoder
# from modules.dane import data_new
from flasgger import swag_from

# import modules.movies

app = Flask(__name__)
api = Api(app)
app.json_encoder = LazyJSONEncoder

swagger_template = dict(
    info={
        'title': LazyString(lambda: 'My first Swagger UI document'),
        'version': LazyString(lambda: '0.1'),
        'description': LazyString(
            lambda: 'This document depicts a      sample Swagger UI document and implements Hello World functionality after executing GET.'), },
    host=LazyString(lambda: request.host))
swagger_config = {"headers": [],
                  "specs": [
                      {"endpoint": 'hello',
                       "route": '/hello.yml',
                       "rule_filter": lambda rule: True,
                       "model_filter": lambda tag: True, }
                  ],
                  "static_url_path": "/flasgger_static", "swagger_ui": True,
                  "specs_route": "/apidocs/"}

swagger = Swagger(app, template=swagger_template, config=swagger_config)


@swag_from("hello.yml", methods=['GET'])
@app.route("/")
def hello():
    return "Hello World!!!"


"""class Links(Resource):
    def get(self):
        return data_new('modules/links.csv')"""

# api.add_resource(HelloWorld, '/')
# api.add_resource(Links, '/links')

if __name__ == '__main__':
    app.run(debug=True)
