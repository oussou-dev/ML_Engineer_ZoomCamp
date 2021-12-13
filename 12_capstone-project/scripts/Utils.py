import pandas as pd
import numpy as np


def read_dataset(path):
    df = pd.read_csv(path)
    return df


def merge_dataframes(df1, df2, col_name):
    combined_data = pd.merge(df1, df2, on=col_name)
    return combined_data


def remove_outliers(df, col, thresh):
    df = df.drop(df.loc[df[col] > thresh].index)
    return df


def year_from_date(df, date_col, new_col_name='year'):
    if new_col_name in df:
        raise KeyError(
            f"{new_col_name} column already exists. Please enter a different value for new_col_name")
    df[new_col_name] = pd.DatetimeIndex(df[date_col]).year
    return df


def month_from_date(df, date_col, new_col_name='month'):
    if new_col_name in df:
        raise KeyError(
            f"{new_col_name} column already exists. Please enter a different value for new_col_name")
    df[new_col_name] = pd.DatetimeIndex(df[date_col]).month
    return df
