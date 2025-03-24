from itertools import chain
from random import choice


class RandomLooper:
    def __init__(self, *seq):
        self.iters = list(chain(*map(iter, seq)))

    def __iter__(self):
        return self

    def __next__(self):
        if not self.iters:
            raise StopIteration
        return self.iters.pop(self.iters.index(choice(self.iters)))



randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])

print(list(randomlooper))
print(list(randomlooper))
