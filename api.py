from flask import Flask, request, redirect, url_for, render_template
from flask_restful import Resource, Api
from flasgger import LazyString
from flasgger import Swagger, LazyJSONEncoder
# from modules.dane import data_new
from flasgger import swag_from
from modules.sus import entropia, dane_wyjsciowe

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
                       "model_filter": lambda tag: True, },
                      {"endpoint": 'test',
                       "route": '/test.yml',
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


@app.route('/success/<wynik>')
def success(wynik):
    return wynik


@swag_from("test.yml", methods=['Post'])
@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        lista=[list(k.split(",")) for k in request.form['nm'].split()]

        #print(lista)
        wynik = dane_wyjsciowe(lista)
        # print(wynik)
        #wynik = 2
        return redirect(url_for('success', wynik=wynik))
        #return wynik
    else:
        wynik = request.args.get('nm')
        return redirect(url_for('success', wynik=wynik))


@app.route('/ent')
def ent():
    return render_template('entropia.html')


"""class Links(Resource):
    def get(self):
        return data_new('modules/links.csv')"""

# api.add_resource(HelloWorld, '/')
# api.add_resource(Links, '/links')

if __name__ == '__main__':
    app.run(debug=True)
