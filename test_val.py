import os
from val_model import validate
from train_model import get_data

def test_model(clean_data):
    _, test_df = get_data('./')
    validate(test_df,'./')

    assert os.path.isfile("./models/slice_output.txt")