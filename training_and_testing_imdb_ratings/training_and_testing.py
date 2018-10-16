import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.cross_validation import StratifiedKFold


def training_and_testing(X_inputfile, Y_inputfile):

    input_features = pd.read_csv(X_inputfile)

    X_values = input_features.as_matrix()

    target_values = pd.read_csv(Y_inputfile)

    #lab_enc = preprocessing.LabelEncoder()
    Y_values = target_values.as_matrix()
    #Y_values = lab_enc.fit_transform(Y_values)

    X_train,X_test, Y_train, Y_test = train_test_split(X_values,Y_values, train_size = 0.7)

    random_forest_clf = RandomForestRegressor(n_estimators=110, max_features='auto', max_depth=300, oob_score=True, min_impurity_decrease=0.000)

    model = random_forest_clf.fit(X_train,Y_train)

    #print(random_forest_clf.feature_importances_)

    print(X_train.shape)
    print(model.score(X_train, Y_train))
    print(model.score(X_test,Y_test))

    predictions = random_forest_clf.predict(X_test)

    plt.scatter(list(predictions), list(Y_test))
    plt.xlabel("imdb rating")
    plt.ylabel("error rate")
    plt.legend(loc="upper right")
    plt.show()

