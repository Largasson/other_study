from collections import UserString


class MutableString(UserString):
    def lower(self):
        self.data = self.data.lower()

    def upper(self):
        self.data = self.data.upper()

    def sort(self, key=None, reverse=None):
        str_lst = list(self.data)
        str_lst.sort(key=key, reverse=reverse)
        self.data = ''.join(str_lst)

    def __setitem__(self, key, value):
        str_lst = list(self.data)
        str_lst[key] = value
        self.data = ''.join(str_lst)

    def __delitem__(self, key):
        str_lst = list(self.data)
        del str_lst[key]
        self.data = ''.join(str_lst)


mutablestring = MutableString('beegeek')

print(mutablestring)
mutablestring[0] = 'B'
mutablestring[-4] = 'G'
print(mutablestring)