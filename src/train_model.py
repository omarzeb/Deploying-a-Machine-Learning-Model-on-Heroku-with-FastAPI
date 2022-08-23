# Script to train machine learning model.

from sklearn.model_selection import train_test_split
import os
import pandas as pd
import pickle

# Add the necessary imports for the starter code.
from ml.data import process_data
from ml.model import train_model

# Add code to load in the data.
def get_data(path):
    csv_path = os.path.join(path, "data", "clean", "census.csv")
    
    df = pd.read_csv(csv_path)
    train_df, test_df = train_test_split(df, test_size=0.20)

    return train_df, test_df

# Optional enhancement, use K-fold cross validation instead of a train-test split.

def model_training(train):
    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]
    X_train, y_train, encoder, lb = process_data(
        train, categorical_features=cat_features, label="salary", training=True
    )

    trained_model = train_model(X_train, y_train)
    pickle.dump(trained_model, open("./models/model.pkl", 'wb'))
    pickle.dump(encoder, open("./models/encoder.pkl", 'wb'))
    pickle.dump(lb, open("./models/lb.pkl", 'wb'))
# Proces the test data with the process_data function.

# Train and save a model.
