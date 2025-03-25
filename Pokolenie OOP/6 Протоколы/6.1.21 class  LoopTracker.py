class LoopTracker:
    def __init__(self, iterable):
        self.iter = iterable
        self._iter = iter(iterable)
        self._count = 0
        self._empty_count = 0
        self._first = list(iterable)[0] if iterable else AttributeError("Исходный итерируемый объект пуст")
        self._last = AttributeError("Последнего элемента нет")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self._count < len(self.iter):
                self._count += 1
            self._last = next(self._iter)
            return self._last
        except StopIteration as err:
            self._empty_count += 1
            raise

    def is_empty(self):
        if self._count == len(self.iter):
            return True
        else:
            return False

    accesses = property(lambda self: self._count)
    empty_accesses = property(lambda self: self._empty_count)
    first = property(lambda self: self._first)
    last = property(lambda self: self._last)


# TEST_12:
loop_tracker = LoopTracker(dict.fromkeys(range(100)))

print(next(loop_tracker))
print(next(loop_tracker))
print(next(loop_tracker))
print(loop_tracker.accesses)
print(loop_tracker.first)
print(loop_tracker.last)
print(loop_tracker.is_empty())

# TEST_13:
loop_tracker = LoopTracker([1, 2, 3])

try:
    loop_tracker.accesses = 1
except AttributeError as e:
    print(type(e))

try:
    loop_tracker.first = 1
except AttributeError as e:
    print(type(e))

try:
    loop_tracker.last = 1
except AttributeError as e:
    print(type(e))
