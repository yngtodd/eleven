"""Test the functions in our math.py module"""

from eleven import math


def test_add_negative():
    assert math.add_one(-1) == 0


def test_add_positive():
    assert math.add_one(1) == 2


def test_halve():
    assert math.halve(2.0) == 1.0


def test_halve_int():
    assert math.halve(4) == 2
