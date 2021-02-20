class KdeModel:

    def __init__(self, kde_model, kernel: str, bandwidth: float, problem_name, graph_type, number_of_instances_trained,
                 p: int):
        self.kde_model = kde_model
        self.kernel = kernel
        self.bandwidth = bandwidth
        self.problem_name = problem_name
        self.graph_type = graph_type
        self.number_of_instances_trained = number_of_instances_trained
        self.p = p
