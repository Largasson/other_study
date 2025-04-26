from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        self.seq = []
        for elem in args:
            if isinstance(elem, int):
                self.seq.append(elem)
            elif isinstance(elem, str):
                start, end = elem.split('-')
                self.seq.extend(range(int(start), int(end) + 1))

    def __contains__(self, elem):
        return elem in self.seq

    def __len__(self):
        return len(self.seq)

    def __getitem__(self, key):
        return self.seq[key]


customrange = CustomRange()

print(len(customrange))
print(*customrange)
print(*reversed(customrange))
