class OrderedSet:
    def __init__(self, iterable=None):
        self._dict = {}
        if iterable:
            for item in iterable:
                self.add(item)

    def add(self, item):
        self._dict[item] = None

    def discard(self, item):
        if item in self._dict:
            self._dict.pop(item)

    def __len__(self):
        return len(self._dict)

    def __iter__(self):
        yield from self._dict

    def __contains__(self, item):
        return item in self._dict

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return list(self._dict) == list(other._dict)
        elif isinstance(other, set):
            return set(self._dict) == other
        else:
            return NotImplemented



# TEST_4:
print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['green', 'red', 'blue']))
print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['red', 'blue', 'green']))
print(OrderedSet(['green', 'red', 'blue']) == {'blue', 'red', 'green'})
print(OrderedSet(['green', 'red', 'blue']) == ['green', 'red', 'blue'])
print(OrderedSet(['green', 'red', 'blue']) == 100)

# TEST_5:
data = ['Ada Lovelace'] * 1000
orderedset = OrderedSet(data)

print(len(orderedset))

# TEST_6:
orderedset = OrderedSet([1, 2, 3, 4])
not_supported = [120, {1: 'one'}, True, 'pi = 3', 17.9]

for item in not_supported:
    print(item != orderedset)

# TEST_7:
orderedset = OrderedSet([1, 2, 3, 4])
print(orderedset.__eq__(1))
print(orderedset.__ne__(1.1))