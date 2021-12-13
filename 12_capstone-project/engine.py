from sklearn.model_selection import train_test_split
from scripts.Utils import read_dataset
from scripts.Utils import merge_dataframes
from scripts.Utils import remove_outliers
from scripts.Utils import year_from_date
from scripts.Impute import impute
from scripts.Cat_to_num import cat_to_num
from scripts.Utils import month_from_date
from scripts.Train_model import train_model
from scripts.Evaluate_results import evaluate_results
from scripts.Feature_importance import feature_importance
import pandas as pd
import numpy as np
import joblib

# Reading the data
store_details = read_dataset("/workspaces/ML_Engineer_ZoomCamp/12_capstone-project/data/store.csv")
train_data = read_dataset("/workspaces/ML_Engineer_ZoomCamp/12_capstone-project/data/train.csv")

# Combining 2 dataframes
combined_data = merge_dataframes(store_details, train_data, 'Store')

# Imputation
store_details = impute(store_details, 'Promo2SinceWeek', method='value')
store_details = impute(store_details, 'Promo2SinceYear', method='value')
store_details = impute(store_details, 'PromoInterval', method='value')
store_details = impute(store_details, 'CompetitionDistance', method='mean')
store_details = impute(
    store_details, 'CompetitionOpenSinceMonth', method='mode')
store_details = impute(
    store_details, 'CompetitionOpenSinceYear', method='mode')
combined_data = merge_dataframes(train_data, store_details, 'Store')

# Remove outliers
combined_data = remove_outliers(combined_data, 'Sales',  30000)

# Removing Exceptions
combined_data.drop(combined_data.loc[(combined_data['Sales'] == 0) & (combined_data['Open'] == 1) &
                                     (combined_data['StateHoliday'] == 0) &
                                     (combined_data['SchoolHoliday'] == 0)].index, inplace=True)
# Extract year from date
combined_data = year_from_date(combined_data, 'Date', 'Year')

# Extract month from date
combined_data = month_from_date(combined_data, 'Date', 'Month')

# Catagorical to numerical
combined_data = cat_to_num(combined_data, 'Assortment', 'default')
combined_data = cat_to_num(combined_data, 'StoreType', 'default')
impute_dict = {
    "Jan,Apr,Jul,Oct": 1,
    "Feb,May,Aug,Nov": 2,
    "Mar,Jun,Sept,Dec": 3
}
combined_data = cat_to_num(
    combined_data, 'PromoInterval', 'custom', values=impute_dict)
impute_dict_2 = {
    'a': 1,
    'b': 2,
    'c': 3
}
combined_data = cat_to_num(
    combined_data, 'StateHoliday', 'custom', values=impute_dict_2)

# Convert to numeric
combined_data['StateHoliday'] = pd.to_numeric(combined_data['StateHoliday'])
combined_data['PromoInterval'] = pd.to_numeric(combined_data['PromoInterval'])

# Train test split
combined_data_subset = combined_data[combined_data['Open'] == 1]
combined_data_subset_closed = combined_data[combined_data['Open'] == 0]
x_train, x_test, y_train, y_test_open = train_test_split(combined_data_subset.drop(
    ['Sales', 'Customers', 'Open', 'Date'], axis=1), combined_data_subset['Sales'], test_size=0.20)

# Model building
pred = train_model(x_train, x_test, y_train, y_test_open,
                   'RF_reg', '/workspaces/ML_Engineer_ZoomCamp/12_capstone-project/models/rf.pkl')

prediction_closed = np.zeros(combined_data_subset_closed.shape[0])
prediction = np.append(pred, prediction_closed)
y_test = np.append(y_test_open, np.zeros(combined_data_subset_closed.shape[0]))

# Evaluate model
results = evaluate_results(y_test, prediction)

model = joblib.load('/workspaces/ML_Engineer_ZoomCamp/12_capstone-project/models/dt.pkl')
fi = feature_importance(x_train.columns, model)
