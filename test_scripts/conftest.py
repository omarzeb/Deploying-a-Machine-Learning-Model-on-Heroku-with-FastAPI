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

    print("low dataframe")
    print(df)
    return df


@pytest.fixture
def inference_data_high():
    data_dict = {'age': 33,
                 'workclass': 'Private',
                 'fnlgt': 149184,
                 'education': 'HS-grad',
                 'marital-status': 'Never-married',
                 'occupation': 'Prof-specialty',
                 'relationship': 'Not-in-family',
                 'race': 'White',
                 'sex': 'Male',
                 'hours-per-week': 60,
                 'native-country': 'United-States'
                 }
    df = pd.DataFrame(data=data_dict.values(),
                      index=data_dict.keys()).T
    print("high dataframe")
    print(df)
    return df


@pytest.fixture
def client():
    api_client = TestClient(app)
    return api_client
