[![Unitary Fund](https://img.shields.io/badge/Supported%20By-UNITARY%20FUND-brightgreen.svg?style=for-the-badge)](http://unitary.fund)
# QaoaParamsPredictorApi

Note: This project is <b>still in progress</b>! Some TODOs which are currently being addressed:

 - Storing machine learning models in Cloud Storage.
 - Storing Cloud Storage addresses of machine learning models in a MySQL database (Cloud SQL).
 - Communication of the API with the database and the Cloud Storage.
 - Tests of the API (Postman).

You can find the draft of a system architecture below:

<a href="https://ibb.co/7Gs3TJ1"><img src="https://i.ibb.co/nDxXVsL/kde-api-drawio-1.png" alt="kde-api-drawio-1" border="0"></a>

The minimal and functional deployment of the API is available here:
https://qaoa-params-predictor-api-5uo2z7eykq-uc.a.run.app/. You can play with it manually by clicking the 'Try it out' button.
The stable_set option is not supplied with files on purpose and serves as a demonstration of the reaction to a request for a non-existent resource.

This API provides (hopefully) good input parameters for variational quantum algorithms for various types of combinatorial optimization problems. It allows to skip computationally expensive classical optimization over a parameter's space at still obtain a reasonably good solution. The current focus of the API is the Quantum Approximate Optimization Algorithm (QAOA) with a default ansatz (see Fahri et al. https://arxiv.org/abs/1411.4028).

The API provides an endpoint powered by machine learning models trained using a Kernel Density Estimation algorithm. Models were trained using the Kernel Density Estimation algorithmon a big number of good input parameters sets, specific to an optimization problem and the class of a graph. They were obtained by solving the QAOA algorithm with a classical optimization loop in the cloud, initialized at several thousands of random points in the parameters space for each problem instance. Parameters sets that yielded solutions of a poor quality were discarded from the training set. We followed the methodology of Khairy et al. (https://arxiv.org/abs/1911.11071).

In our API, the following optimization problems are supported: MaxCut, Graph Partition, Vertex Cover, Stable Set, for the following classes of graphs: Erdos-Renyi, caveman, barbell, ladder, for the following depths of quantum circuits: p=1, p=2, p=3 and p=4.

The project is funded by the Unitary Fund and computational resources in the cloud were provided by Zapata Computing.

This project is licensed under the terms of the Apache 2.0 license.
