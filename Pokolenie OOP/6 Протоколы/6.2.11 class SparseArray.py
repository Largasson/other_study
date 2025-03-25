class SparseArray:
    def __init__(self, default=None):
        self._dict = {}
        self._default = default


    def __setitem__(self, key, value):
        self._dict[key] = value

    def __getitem__(self, key):
        return self._dict.get(key, self._default)

array = SparseArray(None)

array[0] = 'Timur'
array[1] = 'Arthur'

print(array[0])
print(array[1])
print(array[2])