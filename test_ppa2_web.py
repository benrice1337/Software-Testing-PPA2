from ppa2webservice import *
import pytest
from unittest import mock

def test_calcbmi():
    with mock.patch('flask.request') as request_mock:
        request_mock.form = {'feet': '5', 'inches': '8', 'pounds': '140'}
        assert 'Normal' in calc_bmi()
