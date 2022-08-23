import os
import sys
from src.val_model import validate
from src.train_model import get_data

def test_model(clean_data):
    _, test_df = get_data('./')
    validate(test_df,'./')

    assert os.path.isfile(sys.path[0] + "/../models/slice_output.txt")