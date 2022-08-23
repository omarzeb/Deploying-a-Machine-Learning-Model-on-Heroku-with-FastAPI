import pickle
import sys
from ml.data import process_data
from ml.model import inference


def run_inference(data):
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
    trained_model = pickle.load(open(sys.path[0] + "/../models/model.pkl", 'rb'))
    encoder = pickle.load(open(sys.path[0] + "/../models/encoder.pkl", 'rb'))
    lb = pickle.load(open(sys.path[0] + "/../models/lb.pkl", 'rb'))

    X, _, _, _ = process_data(
        data,
        categorical_features=cat_features,
        encoder=encoder, lb=lb, training=False)

    pred = inference(trained_model, X)
    prediction = lb.inverse_transform(pred)[0]

    return prediction