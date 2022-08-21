import pickle
from ml.model import compute_score_per_slice
import os

def validate(test_df, path):
   
    # load model and encoder
    trained_model = pickle.load(open(os.path.join(path,"models/model.pkl"), 'rb'))
    encoder = pickle.load(open(os.path.join(path,"models/encoder.pkl"), 'rb'))
    lb = pickle.load(open(os.path.join(path,"models/lb.pkl"), 'rb'))

    compute_score_per_slice(
        trained_model,
        test_df,
        encoder,
        lb,
        path)