import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
import math
import joblib


def train_model(x_train, x_test, y_train, y_test, model_name, path):
    model_dict = {
        'linear_reg': LinearRegression,
        'RF_reg': RandomForestRegressor,
        'dtree_reg': DecisionTreeRegressor,
    }
    if model_name not in list(model_dict.keys()):
        raise ValueError(
            f"Only these options for model_name are allowed : {list(model_dict.keys())}")
    model = model_dict[model_name]()
    model.fit(x_train, y_train)
    pred = model.predict(x_test)
    # Save the model as a pickle in a file
    # filename = 'output/'+ str(model_name) + '.pkl'
    joblib.dump(model, path)
    print('Model saved as pkl file in '+str(path))
    return pred
