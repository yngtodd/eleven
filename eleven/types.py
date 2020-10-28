class Container:
    """Container for data"""

    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        return self.data == other.data
