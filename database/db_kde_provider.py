# TODO likely not necessary because we only need the address for internal processing
# @kde_ns.route("/", methods=["GET"])
# def index(db, p: int, problem_name, graph_type):
#     model_address_json = get_kde_model_addres(db, p , problem_name, graph_type)
#     return model_address_json
from exceptions.mysql_kde_model_exception import MySqlKdeModelException


def get_kde_model_address(db, problem_name: str, graph_type: str, p_depth: int):
    with db.connect() as conn:
        # Execute the query and fetch all results
        model_address = conn.execute(
            f"SELECT model_address FROM models WHERE problem_name={problem_name} AND p={p_depth} AND graph_type="
            f"{graph_type}"
        ).fetchall()
        if len(model_address) < 1:
            raise MySqlKdeModelException(
                f"Address for a requested KDE model with problem_name={problem_name}, p={p_depth}, graph_type="
                f"{graph_type} not found in the database.")
        if len(model_address) > 1:
            raise MySqlKdeModelException(
                f"More than one address for a requested KDE model with problem_name={problem_name}, p={p_depth}, "
                f"graph_type="
                f"{graph_type} found in the database.")
        model_address = model_address[0]
    return model_address
