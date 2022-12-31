import dill

from database.db_kde_provider import get_kde_model_address


def get_kde_model(db, problem_name: str, graph_type: str, p_depth: int, bucket_name, blob_name):

    kde_model_address = get_kde_model_address(db, problem_name, graph_type, p_depth)
    kde_model = _get_kde_model_from_cloud_storage(kde_model_address, bucket_name, blob_name)

    return kde_model


def _get_kde_model_from_cloud_storage(storage_client, bucket_name, blob_name):

    """Write and read a blob from GCS using file-like IO. Undill the file and return the model as a Python object."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The ID of your new GCS object
    # blob_name = "storage-object-name"

    # blob_name argument that you pass to cloudstorage.open() is the path to your file in YOUR_BUCKET_NAME/PATH_IN_GCS format

    # storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    with blob.open("r") as f:

        try:
            kde_model = dill.load(f)
            # TODO specify exception
        except:
            raise Exception("Cannot unpickle a kde_model.")

    return kde_model
