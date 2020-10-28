import pytest

from eleven.examples import function_with_exception


def test_function_raises_exception(negative_value):
    with pytest.raises(ValueError):
        function_with_exception(negative_value)


def test_function_returns_val(positive_value):
    val_returned = function_with_exception(positive_value)
    assert val_returned == positive_value

