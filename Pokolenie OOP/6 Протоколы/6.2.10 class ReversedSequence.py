class ReversedSequence:
    def __init__(self, sequence):
        self._sequence = sequence


    def __len__(self):
        return len(self._sequence)

    def __iter__(self):
        yield from self._sequence[::-1]

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Index must be an integer")
        if key < 0 or key >= len(self):
            raise IndexError("Index out of range")
        return self._sequence[::-1][key]

reversed_numbers = ReversedSequence((1, 2, 3, 4, 5))

for num in reversed_numbers:
    print(num)
