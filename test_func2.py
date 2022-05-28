import pytest
import pandas as pd
from func2 import create_dataset, get_prediction
import numpy as np



@pytest.fixture
def dataset_test():
    data = {
        'YearBuilt': 1960,
        'YearRemodAdd': 1960,
        'Pool' : False,
        'Fence': False,
        'ScreenPorch':0,
        'OpenPorchSF':62,
        'EnclosedPorch':0,
        'WoodDeckSF':210,
        'GarageArea': 528,
        'LotArea': 31770,
        'TotalBsmtSF':1080,
        'FstFlrSF':1656,
        'SndFlrSF':0,
        'GrLivArea': 1656,
        'FullBath':1,
        'BedroomAbvGr':3,
        'KitchenAbvGr':1,
        'TotRmsAbvGrd':7,
        'Fireplaces':2,
        'GarageCars':2,
        'LotFrontage': 141
    }
    dataset_test = pd.DataFrame(data, index=[0])
    return dataset_test


def test_create_dataset():
    data = {
        'YearBuilt': 1960,
        'YearRemodAdd': 1960,
        'Pool' : False,
        'Fence': False,
        'ScreenPorch':0,
        'OpenPorchSF':62,
        'EnclosedPorch':0,
        'WoodDeckSF':210,
        'GarageArea': 528,
        'LotArea': 31770,
        'TotalBsmtSF':1080,
        'FstFlrSF':1656,
        'SndFlrSF':0,
        'GrLivArea': 1656,
        'FullBath':1,
        'BedroomAbvGr':3,
        'KitchenAbvGr':1,
        'TotRmsAbvGrd':7,
        'Fireplaces':2,
        'GarageCars':2,
        'LotFrontage': 141
    }
    dataset =create_dataset(data)
    assert dataset['ScreenPorch'][0] == 0
    assert dataset['OpenPorchSF'][0] == 62
    assert dataset['WoodDeckSF'][0] == 210
    assert dataset['EnclosedPorch'][0] == 0
    assert dataset['GarageCars'][0] == 2
    assert dataset['Fireplaces'][0] == 2
    assert dataset['YearBuilt'][0] == 1960
    assert dataset['YearRemodAdd'][0] == 1960
    assert dataset['LotArea'][0] == 31770
    assert dataset['GrLivArea'][0] == 1656
    assert dataset['TotalBsmtSF'][0] == 1080
    assert dataset['FstFlrSF'][0] == 1656
    assert dataset['SndFlrSF'][0] == 0
    assert dataset['LotFrontage'][0] == 141
    assert dataset['GarageArea'][0] == 528
    assert dataset['TotRmsAbvGrd'][0] == 7
    assert dataset['FullBath'][0] == 1
    assert dataset['BedroomAbvGr'][0] == 3
    assert dataset['KitchenAbvGr'][0] == 1
    assert dataset['Fence'][0] == False
    assert dataset['Pool'][0] == False


def test_get_prediction(dataset_test):
    prediction = get_prediction(dataset_test)
    assert type(prediction) == np.ndarray

