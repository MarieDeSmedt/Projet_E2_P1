import pytest
import pandas as pd
from func2 import create_dataset, get_prediction
import numpy as np

@pytest.fixture
def dataset_test():
    data = {'Age': 20,
        'GrLivArea':100,
        'LotFrontage': 100,
        'LotArea': 100,
        'GarageArea': 100,
        'Fence': False,
        'Pool' : True
        }
    dataset_test = pd.DataFrame(data, index=[0])
    return dataset_test


def test_create_dataset():
    data =create_dataset(20,100,100,100,100,False,True)
    assert data['Age'][0] == 20
    assert data['GrLivArea'][0] == 100
    assert data['LotFrontage'][0] == 100
    assert data['LotArea'][0] == 100
    assert data['GarageArea'][0] == 100
    assert data['Fence'][0] == False
    assert data['Pool'][0] == True

def test_get_prediction(dataset_test):
    prediction = get_prediction(dataset_test)
    assert type(prediction) == np.ndarray

