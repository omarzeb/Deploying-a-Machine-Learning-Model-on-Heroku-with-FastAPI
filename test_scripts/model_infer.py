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
    trained_model = pickle.load(open("./models/model.pkl", 'rb'))
    encoder = pickle.load(open("./models/encoder.pkl", 'rb'))
    lb = pickle.load(open("./models/lb.pkl", 'rb'))

    X, _, _, _ = process_data(
        data,
        categorical_features=cat_features,
        encoder=encoder, lb=lb, training=False)

    pred = inference(trained_model, X)
    prediction = lb.inverse_transform(pred)[0]
    print(prediction)

    return prediction
