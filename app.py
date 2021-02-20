import dill

from flask import Flask
from flask_restx import Api, reqparse, Resource

app = Flask(__name__)

api = Api(app, title='QAOA params predictor API', description='API for predicting QAOA params.')

ns = api.namespace('KDE models', description='Trained KDE models')


@ns.route('/')
@ns.param('problem_name', 'Problem name')
@ns.param('graph_type', 'Graph type')
@ns.param('p_depth', 'Depth-related p parameter')
@ns.param('num_samples', 'Number of samples')
class KdeModels(Resource):

    @ns.doc('Get predicted parameters.')
    def post(self):
        """Returns parameters sampled from the KDE model base on arguments provided."""
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('problem_name', type=str, required=True)  # add args
        parser.add_argument('graph_type', type=str, required=True)
        parser.add_argument('p_depth', type=int, required=True)
        parser.add_argument('num_samples', type=int, required=True)

        args = parser.parse_args()  # parse arguments to dictionary

        example_model_path = "serialized_models/kde_model_max_cut_random_gaussian_bandwidth=0.2_p=1"
        example_model = dill.load(open(example_model_path, 'rb'))

        problem_name = args['problem_name']
        graph_type = args['graph_type']
        p_depth = args['p_depth']
        num_samples = args['num_samples']

        sampled_params = []

        for _ in range(num_samples):
            sampled_params.append(example_model.kde_model.sample().tolist())

        # add the newly provided values

        return {'sampled_params': sampled_params}, 200  # return data with 200 OK


if __name__ == '__main__':
    app.run()  # run our Flask app
