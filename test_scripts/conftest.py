import pytest
import pandas as pd
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def clean_data():
    """
    Get dataset
    """
    df = pd.read_csv("./data/clean/census.csv")
    return df



@pytest.fixture
def train_data(clean_data):

    df = clean_data.drop('salary', axis=1)
    return df


@pytest.fixture
def test_data(clean_data):

    df = clean_data['salary']
    return df


@pytest.fixture
def inference_data_low():
    data_dict = {'age': 19,
                 'workclass': 'Private',
                 'fnlgt': 77516,
                 'education': 'HS-grad',
                 'marital-status': 'Never-married',
                 'occupation': 'Own-child',
                 'relationship': 'Husband',
                 'race': 'Black',
                 'sex': 'Male',
                 'hours-per-week': 40,
                 'native-country': 'United-States'
                 }
    df = pd.DataFrame(data=data_dict.values(),
                      index=data_dict.keys()).T

    return df

# 37   Private  280464   Some-college   Married-civ-spouse   Exec-managerial      Husband   Black   Male             80   United-States
@pytest.fixture
def inference_data_high():

    data_dict = {'age': 52,
                 'workclass': ' Self-emp-not-inc',
                 'fnlgt': 209642,
                 'education': ' HS-grad',
                 'marital-status': ' Married-civ-spouse',
                 'occupation': ' Exec-managerial',
                 'relationship': ' Husband',
                 'race': ' White',
                 'sex': ' Male',
                 'hours-per-week': 45,
                 'native-country': ' United-States'
                 }
    df = pd.DataFrame(data=data_dict.values(),
                    index=data_dict.keys()).T

    return df


@pytest.fixture
def client():
    api_client = TestClient(app)
    return api_client
