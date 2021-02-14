from flask import Flask
from flask_restful import Api

from kde_model import KdeModels

if __name__ == '__main__':
    app = Flask("API")
    api = Api(app)


    @app.route('/', methods=['GET'])
    def home():
        return "<h1>QAOA initialization API</h1><p>This site is a prototype API for finding good starting parameters " \
               "for the QAOA.</p> "

    api.add_resource(KdeModels, '/kde')

    app.run()  # run our Flask app
