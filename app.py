from flask import Flask
from flask_restx import Api, reqparse, Resource

from exceptions.kde_model_not_found_exception import KdeModelNotFoundException
from kde_models_provider import get_kde_model

app = Flask(__name__)

api = Api(app, title='QAOA params predictor API', description='API for predicting QAOA params.')

ns = api.namespace('KDE models', description='Trained KDE models')
parser = reqparse.RequestParser()
parser.add_argument('problem_name', type=str, required=True, choices=("max_cut", "stable_set"))  # add args
parser.add_argument('graph_type', type=str, required=True, choices=("random", "caveman"))
parser.add_argument('p_depth', type=int, required=True, choices=(1, 2, 3, 4))
parser.add_argument('num_samples', type=int, required=True)


@ns.route('/')
class KdeModels(Resource):

    @ns.doc('Get predicted parameters.')
    @ns.expect(parser, validate=True)
    def post(self):
        """Returns parameters sampled from the KDE model base on arguments provided."""

        problem_name, graph_type, p_depth, num_samples = self._parse_arguments(parser)

        directory = "/serialized_models/"

        try:
            relevant_kde_model = get_kde_model(directory, problem_name, graph_type, p_depth)
        except KdeModelNotFoundException as err:
            return 'KDE model with given parameters not found.', 400

        sampled_params = []

        for _ in range(num_samples):
            sampled_params.append(relevant_kde_model.kde_model.sample().tolist())

        # add the newly provided values

        return {'sampled_params': sampled_params}, 200  # return data with 200 OK

    def _parse_arguments(self, parser):
        # initialize

        args = parser.parse_args()  # parse arguments to dictionary

        problem_name = args['problem_name']
        graph_type = args['graph_type']
        p_depth = args['p_depth']
        num_samples = args['num_samples']

        return problem_name, graph_type, p_depth, num_samples


if __name__ == '__main__':
    app.run()  # run our Flask app
