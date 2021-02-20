from flask import Flask
from flask_restx import Api, reqparse, Resource

app = Flask(__name__)

api = Api(app, title='QAOA params predictor API', description='API for predicting QAOA params.')

ns = api.namespace('KDE models', description='Trained KDE models')


@ns.route('/')
@ns.param('problem_name', 'Problem name')
@ns.param('graph_type', 'Graph type')
@ns.param('p_depth', 'Depth-related p parameter')
class KdeModels(Resource):

    @ns.doc('Get predicted parameters.')
    def post(self):
        """Returns parameters sampled from the KDE model base on arguments provided."""
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('problem_name', required=True)  # add args
        parser.add_argument('graph_type', required=True)
        parser.add_argument('p_depth', required=True)
        args = parser.parse_args()  # parse arguments to dictionary

        # add the newly provided values
        sampled_params = []

        return {'sampled_params': sampled_params}, 200  # return data with 200 OK


if __name__ == '__main__':

    app.run()  # run our Flask app
