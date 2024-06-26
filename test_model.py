from pathlib import Path
import logging
import pandas as pd
import pytest
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import load
from model.model_function import process_data


DATA_PATH = 'data/census_cleaned.csv'
MODEL_PATH = 'model/model.joblib'

cat_features = [
    "workclass",
    "education",
    "marital.status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native.country",
]

@pytest.fixture(name='data')
def data():
    """
    Fixture will be used by the unit tests.
    """
    yield pd.read_csv(DATA_PATH)


def test_load_data(data):
    
    """ Check the data received """

    assert isinstance(data, pd.DataFrame)
    assert data.shape[0]>0
    assert data.shape[1]>0


def test_model():

    """ Check model type """

    model = load(MODEL_PATH)
    assert isinstance(model, RandomForestClassifier)


def test_process_data(data):

    """ Test the data split """

    train, _ = train_test_split(data, test_size=0.20)
    X, y, _, _ = process_data(train, cat_features, label='income')
    assert len(X) == len(y)