from collections.abc import Sequence

class TypeSequence(Sequence):
    def __init__(self, values):
        self.values = values
    def __getitem__(self, index):
        value = self.values[index]
        return value, type(value)


data = TypeSequence([10, False, 'beegeek', 3.14])

print(data[1])