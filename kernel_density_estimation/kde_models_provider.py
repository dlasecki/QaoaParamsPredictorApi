import pathlib
from os import listdir
from os.path import isfile, join

import dill

from exceptions.kde_model_not_found_exception import KdeModelNotFoundException


def get_kde_model(directory: str, problem_name: str, graph_type: str, p_depth: int):
    """Loads a dilled KDE model regarding a given problem distance from a directory provided."""
    fn = pathlib.Path(__file__).parent
    directory = str(fn) + directory
    all_file_names = _get_all_file_names(directory)
    unpickled_model = None
    for file_name in all_file_names:
        if _is_file_relevant(all_file_names[0], problem_name, graph_type, p_depth):
            unpickled_model = dill.load(open(directory + file_name, 'rb'))

    if unpickled_model:

        return unpickled_model
    else:
        raise KdeModelNotFoundException("KDE model not found.")


def _is_file_relevant(file_name: str, problem_name: str, graph_type: str, p_depth: int):
    """Check if a filename provided matches the description of a problem instance."""
    return problem_name in file_name and "p=" + str(p_depth) in file_name and graph_type in file_name


def _get_all_file_names(directory: str):
    """Gets all file names from a given directory."""
    return [file_name for file_name in listdir(directory) if isfile(join(directory, file_name))]
