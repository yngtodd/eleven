"""Test the functions in our math.py module"""
import pytest

from eleven import math


@pytest.fixture
def test_value():
   val = 2
   return val


def test_add_negative():
    assert math.add_one(-1) == 0


def test_add_positive(test_value):
    assert math.add_one(1) == test_value


def test_halve():
    assert math.halve(2.0) == 1.0


def test_halve_int(test_value):
    assert math.halve(4) == test_value
