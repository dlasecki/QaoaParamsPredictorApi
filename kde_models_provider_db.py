import dill

from database.db_kde_provider import get_kde_model_address


def get_kde_model(db, problem_name: str, graph_type: str, p_depth: int):

    kde_model_address = get_kde_model_address(db, problem_name, graph_type, p_depth)
    kde_model_binary = _get_kde_model_from_cloud_storage(kde_model_address)

    try:
        unpickled_model = dill.load(kde_model_binary)
    # TODO specify exception
    except:
        raise Exception("Cannot unpickle a kde_model_binary.")

    return unpickled_model


# TODO implement getter from Cloud Storage
def _get_kde_model_from_cloud_storage(address):
    return 0
