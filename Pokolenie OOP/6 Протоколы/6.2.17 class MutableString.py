class MutableString:
    def __init__(self, string=""):
        self.string = string

    def lower(self):
        self.string = self.string.lower()

    def upper(self):
        self.string = self.string.upper()

    def __str__(self):
        return self.string

    def __repr__(self):
        return f"MutableString('{self.string}')"

    def __len__(self):
        return len(self.string)

    def __iter__(self):
        yield from self.string

    def __getitem__(self, key):
        if isinstance(key, int):
            return MutableString(self.string[key])
        elif isinstance(key, slice):
            return MutableString(self.string[key])

    def __setitem__(self, key, value):
        if isinstance(key, int):
            key = len(self.string) + key if key < 0 else key
            self.string = self.string[:key] + value + self.string[key + 1:]
        elif isinstance(key, slice):
            start, stop, step = key.indices(len(self.string))
            self.string = self.string[:start] + value + self.string[stop:]

    def __delitem__(self, key):
        if isinstance(key, int):
            self.string = self.string[:key] + self.string[key + 1:]
        elif isinstance(key, slice):
            del_indexes = tuple(ind for ind in range(key.start, key.stop, key.step or 1))
            self.string = ''.join(char for i, char in enumerate(self.string) if i not in del_indexes)

    def __add__(self, other):
        return MutableString(self.string + other.string)
