# TODO likely not necessary because we only need the address for internal processing
# @kde_ns.route("/", methods=["GET"])
# def index(db, p: int, problem_name, graph_type):
#     model_address_json = get_kde_model_addres(db, p , problem_name, graph_type)
#     return model_address_json


def get_kde_model_addres(db, p: int, problem_name, graph_type):
    with db.connect() as conn:
        # Execute the query and fetch all results
        model_address = conn.execute(
            f"SELECT model_address FROM models WHERE problem_name={problem_name} AND p={p} AND graph_type={graph_type}"
        ).fetchall()
        if len(model_address) < 1:
            raise Exception("Model not found.")
        if len(model_address) > 1:
            raise Exception("More that one model found!.")
        model_address = model_address[0]
    return {
        'model_address': model_address
    }
