import pandas as pd
import numpy as np


def feature_importance(X_train_cols, model):
    feature_importance = model.feature_importances_
    feature_importance_value = []
    for i in range(len(feature_importance)):
        feature_importance_value.append(round(feature_importance[i], 5))
    feature_importance_df = pd.DataFrame({"Features": X_train_cols,
                                          "Values": feature_importance_value})
    feature_importance_df.sort_values(
        by=["Values"], inplace=True, ascending=False)
    return feature_importance_df
