from flask_restful import Resource, reqparse


class KdeModels(Resource):

    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('problem_name', required=True)  # add args
        parser.add_argument('graph_type', required=True)
        parser.add_argument('p_depth', required=True)
        args = parser.parse_args()  # parse arguments to dictionary

        # add the newly provided values
        sampled_params = []

        return {'sampled_params': sampled_params}, 200  # return data with 200 OK

