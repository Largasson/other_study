def quantify(iterable, predicate=None):
    if predicate is None:
        predicate = bool
    return sum(map(predicate, iterable))


iterable = iter(['', 1, 0, (), [[]], [], {1: 2}])

print(quantify(iterable, None))