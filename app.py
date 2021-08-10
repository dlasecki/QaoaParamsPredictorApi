import werkzeug
from flask import Flask
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from kernel_density_estimation.kde_resource import ns as kde_ns

werkzeug.cached_property = werkzeug.utils.cached_property  # it fixes an issue with werkzeug

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)
api = Api(app, title='Input parameters predictor API for quantum variational algorithms.',
          description='This API provides (hopefully) good input parameters for variational quantum algorithms '
                      'for various types of combinatorial optimization problems. It allows to skip computationally '
                      'expensive classical optimization over a parameter\'s space at still obtain a reasonably good '
                      'solution. The current focus of the API is the Quantum Approximate Optimization Algorithm (QAOA) '
                      'with a default ansatz (see Fahri et al. https://arxiv.org/abs/1411.4028). \n\n'
                      'The API provides an endpoint powered by machine learning models trained using a Kernel '
                      'Density Estimation algorithm. Models were trained using the Kernel Density Estimation algorithm'
                      'on a big number of good input parameters sets, specific to an optimization problem '
                      'and the class of a graph. They were obtained by solving the QAOA algorithm '
                      'with a classical optimization loop in the cloud, initialized at several '
                      'thousands of random points in the parameters space for each problem '
                      'instance. Parameters sets that yielded solutions of a poor quality were '
                      'discarded from the training set. We followed the methodology of Khairy '
                      'et al. (https://arxiv.org/abs/1911.11071). \n\n'
                      'In our API, the following optimization problems are supported: MaxCut, '
                      'Graph Partition, Vertex Cover, Stable Set, for the following classes of graphs: Erdos-Renyi, '
                      'caveman, barbell, ladder, for the following depths of quantum circuits: p=1, p=2, p=3 and '
                      'p=4. \n\n'
                      'The project is funded by the Unitary Fund and computational resources in the cloud were '
                      'provided by Zapata Computing.', contact='Dariusz Lasecki')
api.add_namespace(kde_ns)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
