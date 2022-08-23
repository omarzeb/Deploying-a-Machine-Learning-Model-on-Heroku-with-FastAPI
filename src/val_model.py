import pickle
import sys
from ml.model import compute_score_per_slice

def validate(test_df, path):
   
    # load model and encoder
    trained_model = pickle.load(open(sys.path[0] + "/models/model.pkl", 'rb'))
    encoder = pickle.load(open(sys.path[0] + "/models/encoder.pkl", 'rb'))
    lb = pickle.load(open(sys.path[0] + "/models/lb.pkl", 'rb'))

    compute_score_per_slice(
        trained_model,
        test_df,
        encoder,
        lb,
        path)