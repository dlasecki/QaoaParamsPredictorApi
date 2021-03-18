import werkzeug
from flask import Flask
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from kde_resource import ns as kde_ns

werkzeug.cached_property = werkzeug.utils.cached_property  # it fixes an issue with werkzeug

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)
api = Api(app, title='QAOA params predictor API', description='API for predicting QAOA params.')
api.add_namespace(kde_ns)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
