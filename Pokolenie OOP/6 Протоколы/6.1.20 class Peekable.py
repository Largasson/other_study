class Peekable:
    def __init__(self, iterable):
        self._iter = iter(iterable)
        self._next = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._next is not None:
            result = self._next
            self._next = None
            return result
        return next(self._iter)

    def peek(self, default=StopIteration):
        if self._next is None:
            try:
                self._next = next(self._iter)
            except StopIteration:
                if default is StopIteration:
                    raise
                return default
        return self._next


iterator = Peekable('Python')

print(*iterator)
print(iterator.peek(None))