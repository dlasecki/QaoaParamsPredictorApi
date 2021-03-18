from flask_restx import Namespace, reqparse, Resource

from exceptions.kde_model_not_found_exception import KdeModelNotFoundException
from kde_models_provider import get_kde_model

ns = Namespace('KDE models', description='Trained KDE models')


def _set_up_parser():
    problems = ("max_cut", "stable_set", "graph_partition", "vertex_cover")
    p_values = (1, 2, 3, 4)
    graph_types = ("random", "caveman", "barbell", "ladder")

    parser = reqparse.RequestParser()
    parser.add_argument('problem_name', type=str, required=True, choices=problems)  # add args
    parser.add_argument('graph_type', type=str, required=True, choices=graph_types)
    parser.add_argument('p_depth', type=int, required=True, choices=p_values)
    parser.add_argument('num_samples', type=int, required=True, default=1)
    return parser


parser = _set_up_parser()


@ns.route('/')
class KdeModels(Resource):

    @ns.doc('Get predicted parameters.')
    @ns.expect(parser, validate=True)
    def post(self):
        """Returns parameters sampled from the KDE model base on arguments provided."""
        problem_name, graph_type, p_depth, num_samples = self._parse_arguments()

        directory = "/serialized_models/"

        try:
            relevant_kde_model = get_kde_model(directory, problem_name, graph_type, p_depth)
        except KdeModelNotFoundException:
            return 'KDE model with given parameters not found.', 400

        sampled_params = []

        for _ in range(num_samples):
            sampled_params.append(relevant_kde_model.kde_model.sample().tolist())

        # add the newly provided values

        return {'sampled_params': sampled_params}, 200  # return data with 200 OK

    @staticmethod
    def _parse_arguments():
        args = parser.parse_args()  # parse arguments to dictionary

        problem_name = args['problem_name']
        graph_type = args['graph_type']
        p_depth = args['p_depth']
        num_samples = args['num_samples']

        return problem_name, graph_type, p_depth, num_samples
