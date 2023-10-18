import os
import pandas as pd
import numpy as py
import seaborn as sns
import matplotlib.pyplot as plt


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


def correlation_heatmap(df):
    """
        This function is used to Plot a heatmap
    """
    _, ax = plt.subplots(figsize=(14, 12))
    colormap = sns.diverging_palette(220, 10, as_cmap=True)

    _ = sns.heatmap(
        df.corr(),
        cmap=colormap,
        square=True,
        cbar_kws={'shrink': .9},
        ax=ax,
        annot=True,
        linewidths=1.9, vmax=2.1, linecolor='white',
        annot_kws={'fontsize': 12}
    )

    plt.title('Pearson Correlation of Features', y=1.05, size=20)