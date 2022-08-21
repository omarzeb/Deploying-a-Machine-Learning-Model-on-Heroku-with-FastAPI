import os
from train_model import get_data, model_training


def test_get_data():
    train_df, test_df = get_data('./')

    assert train_df.shape[0] > 0
    assert train_df.shape[1] == 12

    assert test_df.shape[0] > 0
    assert test_df.shape[1] == 12


def test_model_training():

    train_df, _ = get_data('./')
    model_training(train_df)

    assert os.path.isfile("./models/model.pkl")
    assert os.path.isfile("./models/encoder.pkl")
    assert os.path.isfile("./models/lb.pkl")