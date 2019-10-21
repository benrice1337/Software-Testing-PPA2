from ppa1 import *
import pytest

def test_bmi():
    assert isinstance(bmi(5, 8, 140), str)
    assert bmi('5', 8, 140) == 'Invalid input'
    assert bmi(-1, 8, 140) == 'Invalid input'
    assert bmi(0, 0, 140) == 'Invalid input'
    assert bmi(5, 8, 0) == 'Invalid input'
    assert 'Underweight' in bmi(5, 8, 100)
    assert 'Normal' in bmi(5, 8, 140)
    assert 'Overweight' in bmi(5, 8, 180)
    assert 'Obese' in bmi(5, 8, 300)


def test_retirement():
    assert isinstance(retirement(23, 100, 100, 100), str)
    assert retirement('23', 100, 100, 100) == 'Invalid input'
    assert retirement(100, 1, 1, 1) == 'Invalid input'
    assert retirement(-1, -1, -1, -1) == 'Invalid input'
    assert retirement(0, 0, 0, 0) == 'Invalid input'
    assert 'dead' in retirement(99, 100, 100, 200)
    assert '24' in retirement(23, 100, 100, 100)


def test_distance():
    assert isinstance(distance(0, 0, 0, 0), str)
    assert distance('0', 0, 0, 0) == 'Invalid input'
    assert '0.0' in distance(0.0, 0.0, 0.0, 0.0)


def test_split_tip():
    assert isinstance(split_tip(2, 100.0), str)
    assert split_tip('2', 100.0) == 'Invalid input'
    assert split_tip(51, 100.0) == 'Invalid input'
