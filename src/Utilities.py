import os
import pandas as pd
import numpy as np


def getfilepath():
    """
        function is used to get path
    """
    ROOT_DIR = os.getcwd()
    ROOT_DIR = os.path.dirname(ROOT_DIR)
    # This is to extract the patent directory from the ful path(ETLSystem)
    DATA_DIR = os.path.join(ROOT_DIR, "data")

    return DATA_DIR


def importdata(filepath):
    """
        function is used to import file to our project
    """
    data = pd.read_csv(filepath)

    return data
