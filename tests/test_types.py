from eleven.types import Container


def test_data_container(positive_value):
    c1 = Container(positive_value)
    c2 = Container(positive_value)
    assert c1 == c2
