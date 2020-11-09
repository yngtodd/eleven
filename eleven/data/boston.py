import pandas as pd

from sklearn import datasets


def load_boston():
    boston = datasets.load_boston()

    # Sklearn uses a dictionary like object to hold its datasets
    X = boston['data']
    y = boston['target']

    feature_names = list(boston.feature_names)

    df = pd.DataFrame(X)
    df.columns = boston.feature_names
    df["PRICE"] = y

    return df


def create_classes(data):
    """Create our classes using thresholds

    This is used as an `apply` function for
    every row in `data`.

    Args:
        data: pandas dataframe
    """
    if data["PRICE"] < 16.:
        return 0
    elif data["PRICE"] >= 16. and data["PRICE"] < 22.:
        return 1
    else:
        return 2


def create_boston_classification():
    """Create a classification problem from Boston housing"""
    boston = load_boston()
    labels = boston.apply(create_classes, axis=1)
    boston = boston.drop("PRICE", axis=1)
    return boston, labels


