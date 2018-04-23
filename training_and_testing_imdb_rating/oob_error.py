import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.datasets import make_classification
from sklearn.cross_validation import StratifiedKFold


def oob_error(X_inputfile, Y_inputfile):
    """
    Args:
        X_inputfile (file): The csv file containing the movie features
        Y_inputfile (file): The csv file containing the movie target

    Yields:
        Plost the out_of_bag error rate against the n_estimators

    Raises:
        IOError: Unable to read file

    """

    RANDOM_STATE = 123
    input_features = pd.read_csv(X_inputfile)

    X_values = input_features.as_matrix()

    target_values = pd.read_csv(Y_inputfile)

    Y_values = target_values.as_matrix()

    X_train,X_test, Y_train, Y_test = train_test_split(X_values,Y_values, train_size = 0.7)

    # Generate a binary classification dataset.
    X_train, Y_train = make_classification(n_samples=500, n_features=25,
                               n_clusters_per_class=1, n_informative=15,
                               random_state=RANDOM_STATE)

    # NOTE: Setting the `warm_start` construction parameter to `True` disables
    # support for parallelized ensembles but is necessary for tracking the OOB
    # error trajectory during training.
    ensemble_clfs = [
        ("RandomForestClassifier, max_features='sqrt'",
            RandomForestClassifier(warm_start=True, oob_score=True,
                                   max_features="sqrt",
                                   random_state=RANDOM_STATE)),
        ("RandomForestClassifier, max_features='log2'",
            RandomForestClassifier(warm_start=True, max_features='log2',
                                   oob_score=True,
                                   random_state=RANDOM_STATE)),
        ("RandomForestClassifier, max_features=None",
            RandomForestClassifier(warm_start=True, max_features=None,
                                   oob_score=True,
                                   random_state=RANDOM_STATE))
    ]

    # Map a classifier name to a list of (<n_estimators>, <error rate>) pairs.
    error_rate = OrderedDict((label, []) for label, _ in ensemble_clfs)

    # Range of `n_estimators` values to explore.
    min_estimators = 100
    max_estimators = 500

    for label, clf in ensemble_clfs:
        for i in range(min_estimators, max_estimators + 1):
            clf.set_params(n_estimators=i)
            clf.fit(X_train, Y_train)

            # Record the OOB error for each `n_estimators=i` setting.
            oob_error = 1 - clf.oob_score_
            error_rate[label].append((i, oob_error))

    # Generate the "OOB error rate" vs. "n_estimators" plot.
    for label, clf_err in error_rate.items():
        xs, ys = zip(*clf_err)
        plt.plot(xs, ys, label=label)

    plt.xlim(min_estimators, max_estimators)
    plt.xlabel("n_estimators")
    plt.ylabel("OOB error rate")
    plt.legend(loc="upper right")
    plt.show()
