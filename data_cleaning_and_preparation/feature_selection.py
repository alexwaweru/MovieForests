import csv
import numpy as np
import pandas as pd
from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb


def continuous_features_selection(X_inputfile, Y_input_file):
    """
    Args:
        X_inputfile (file): The csv file containing the movie features
        Y_inputfile (file): The csv file containing the movie target
    Returns:
        feature_correlation (dict): A dictionary of features as keys and their correlations to the response to as value
    Raises:
        IOError: Unable to read file
    """

    continuos_features = ["duration", "director_facebook_likes", "actor_3_facebook_likes", "actor_1_facebook_likes",
                          "cast_total_facebook_likes", "budget", "actor_2_facebook_likes", "movie_facebook_likes"]
    features = pd.read_csv(X_inputfile)
    gross = pd.read_csv(Y_input_file)
    feature_correlation = {}
    for feature in continuos_features:
        pearsonr_coefficient, pvalue = pearsonr(features[feature].astype(np.int64), gross["gross"].astype(np.int64))
        feature_correlation[feature] = (pearsonr_coefficient, pvalue)
    print(feature_correlation)
    return feature_correlation




def discrete_features_selection(inputfile):
    """
    Args:
        filename (str): The csv file containing the movie metadata
    Returns:
        feature_correlation (dict): A dictionary with keys as title of a categorical features and values as their correlation to the reponse
    Raises:
        IOError: Unable to read file
    """
    pass
