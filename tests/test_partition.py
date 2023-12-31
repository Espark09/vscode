from pytest import *
import random
import fixture
from model import (
    ShufflingSamplePartition,
    countingDealingPartition
)

@fixture
def date():
    samples = [
        {
            "sepal_length": i + 0.1,
            "sepal_width" : i + 0.2,
            "petal_length" : i + 0.3,
            "petal_width" : i + 0.4,
            "species": f"sample {i}",
        }
        for i in range(10)
    ]
    return samples

def test_shufflin(data):
    ssp = ShufflingSamplePartition(data)
    random.seed(42)
    assert len(ssp.training) == 8
    assert len(ssp.testing) == 2
    assert ssp.pop() == {
        'petal_length': 1.3,
        'petal_width' : 1.4,
        'sepal_length' : 1.1,
        'sepal_width' : 1.2,
        'species' : 'sample 1'
    }


def test_shuffling_append(data):
    ssp = ShufflingSamplePartition()
    for row in data:
        ssp.append(row)
    random.seed(42)
    assert len(ssp.training) == 8
    assert len(ssp.testing)  == 2
    assert ssp.pop() == {
        'petal_length': 1.3,
        'petal_width' : 1.4,
        'sepal_length' : 1.1,
        'sepal_width' : 1.2,
        'species' : 'sample 1'
    }     


def test_dealing(data):
    cdp = countingDealingPartition(data)
    assert len(cdp.training) == 8
    assert len(cdp.testing) == 2