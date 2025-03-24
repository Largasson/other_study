class SkipIterator:
    def __init__(self, iterable, n):
        self.iter = iter(iterable)
        self.n = n
        self.is_first = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_first:
            self.is_first = False
            return next(self.iter)
        for _ in range(self.n):
            next(self.iter)

        res = next(self.iter)
        if res is None:
            raise StopIteration
        return res


skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)   # не пропускаем элементы

print(*skipiterator)