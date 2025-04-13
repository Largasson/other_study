class AdvancedList(list):

    def join(self, string=' '):
        return string.join(map(str, self))

    def map(self, func):
        self[:] = map(func, self)
        return self

    def filter(self, func):
        self[:] = filter(func, self)
        return self


advancedlist = AdvancedList([0, 1, 2, '', 3, (), 4, 5, False, {}])
id1 = id(advancedlist)

advancedlist.filter(bool)
id2 = id(advancedlist)

print(advancedlist)
print(id1 == id2)