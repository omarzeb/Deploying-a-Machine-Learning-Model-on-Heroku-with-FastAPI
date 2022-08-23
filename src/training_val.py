import os
from train_model import get_data, model_training
from val_model import validate


def go():
    root_path = os.getcwd()

    train_df, test_df = get_data(root_path)

    model_training(train_df)


    validate(test_df, root_path)


if __name__ == "__main__":

    go()