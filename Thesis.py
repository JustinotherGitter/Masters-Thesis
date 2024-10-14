#! /usr/bin/env python3

import contextlib
import os

import matplotlib.pyplot as plt

# If data_path or save_path are not provided, the default values are used
# try:
#     assert data_path
# except NameError:
#     data_path = 'data/'

# try:
#     assert save_path
# except NameError:
#     save_path = 'figures/'


# Temporary default overwrite
# PLOT_PARAMS = {
#     'figure.figsize': plt.rcParams["figure.figsize"], # inches
#     'figure.dpi': 900,          # dots per inch
#     'figure.subplot.left': 0,   # %
#     'figure.subplot.bottom': 0, # %
#     'figure.subplot.right': 1,  # %
#     'figure.subplot.top': 1,    # %
#     'figure.subplot.wspace': 0, # %
#     'figure.subplot.hspace': 0, # %
#     'image.cmap': 'gray', # str or Colormap
# }


# Custom functions
@contextlib.contextmanager
def new_cd(directory: str | os.PathLike):
    """
    Create a context manager to temporarily change the current working directory.

    Parameters
    ----------
    directory : str | os.PathLike
        Path to the directory to change to.

    See Also
    --------
    https://stackoverflow.com/a/75049063
    """
    cur_dir = os.getcwd()

    # This could raise an exception, but it's probably
    # best to let it propagate and let the caller
    # deal with it, since they requested `directory`
    os.chdir(directory)

    try:
        yield

    finally:
        # This could also raise an exception, but you *really*
        # aren't equipped to figure out what went wrong if the
        # old working directory can't be restored.
        os.chdir(cur_dir)