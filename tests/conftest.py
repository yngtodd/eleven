import pytest

from eleven.types import Container


def pytest_runtest_setup(item):
        """Print what test is being setup"""
        print("setting up", item)


@pytest.fixture(params=[1, 2, 3])
def positive_value(request):
   return request.param


@pytest.fixture(params=[-3, -2, -1])
def negative_value(request):
   return request.param


def pytest_assertrepr_compare(op, left, right):
    """Report which objects are being compared"""
    if isinstance(left, Container) and isinstance(right, Container) and op == "==":
        return [
            "Comparing Container instances:",
            "   vals: {} != {}".format(left.data, right.data),
        ]
