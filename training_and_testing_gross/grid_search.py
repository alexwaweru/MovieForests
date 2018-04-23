import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.cross_validation import StratifiedKFold

def grid_search_classifier(X_inputfile, Y_inputfile):
    input_features = pd.read_csv(X_inputfile)

    X_values = input_features.as_matrix()

    target_values = pd.read_csv(Y_inputfile)

    Y_values = target_values.as_matrix()

    X_train,X_test, Y_train, Y_test = train_test_split(X_values,Y_values)

    parameter_gridsearch = {
                     'max_depth' : [3, 4],  #depth of each decision tree
                     'n_estimators': [50, 20],  #count of decision tree
                     'max_features': ['sqrt', 'auto', 'log2'],
                     'min_samples_split': [2],
                     'min_samples_leaf': [1, 3, 4],
                     'bootstrap': [True, False],
                     }

    randomforest = RandomForestClassifier()
    #crossvalidation = StratifiedKFold(Y_train , n_folds=5)

    gridsearch = GridSearchCV(randomforest,             #grid search for algorithm optimization
                                   scoring='accuracy',
                                   param_grid=parameter_gridsearch,
                                   )


    gridsearch.fit(Y_train, X_train)    #train[0::,0] is as target
    model = gridsearch
    parameters = gridsearch.best_params_

    print('Best Score: {}'.format(gridsearch.best_score_))
