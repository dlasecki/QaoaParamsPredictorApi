import werkzeug
from flask import Flask
from flask_restx import Api

from kde_resource import ns as kde_ns

werkzeug.cached_property = werkzeug.utils.cached_property  # it fixes an issue with werkzeug

app = Flask(__name__)

api = Api(app, title='QAOA params predictor API', description='API for predicting QAOA params.')
api.add_namespace(kde_ns)

if __name__ == '__main__':
    app.run()  # run our Flask app
