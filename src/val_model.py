import pickle
import sys
from ml.model import compute_score_per_slice, save_model_metrics
from ml.data import process_data

def validate(test_df, path):
   
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

    # load model and encoder
    trained_model = pickle.load(open(sys.path[0] + "/models/model.pkl", 'rb'))
    encoder = pickle.load(open(sys.path[0] + "/models/encoder.pkl", 'rb'))
    lb = pickle.load(open(sys.path[0] + "/models/lb.pkl", 'rb'))

    X, _, _, _ = process_data(test_df.iloc[:,:-1],
                                categorical_features=cat_features,
                                encoder=encoder, lb=lb, training=False)

    preds = trained_model.predict(X)
    preds = lb.inverse_transform(preds)
    y = test_df.iloc[:,-1]

    save_model_metrics(y, preds, path)

    compute_score_per_slice(
        trained_model,
        test_df,
        encoder,
        lb,
        path)