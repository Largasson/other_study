class HistoryDict:
    def __init__(self, data=None):
        self._dict = {key: [value] for key, value in data.items()} if data else {}

    def keys(self):
        yield from self._dict.keys()

    def values(self):
        for list_value in self._dict.values():
            yield list_value[-1]

    def items(self):
        for key, list_values in self._dict.items():
            yield key, list_values[-1]

    def history(self, key):
        if key not in self._dict:
            return []
        return self._dict[key]

    def all_history(self):
        return self._dict

    def __len__(self):
        return len(self._dict)

    def __iter__(self):
        return iter(self._dict.keys())

    def __getitem__(self, item):
        return self._dict[item][-1]

    def __setitem__(self, key, value):
        if key not in self._dict:
            self._dict[key] = [value]
        else:
            self._dict[key].append(value)

    def __delitem__(self, key):
        del self._dict[key]



# TEST_8:
historydict = HistoryDict({'name': 'Irenica', 'country': 'Russia', 'level': 'junior', })

print(historydict.all_history())

historydict['country'] = 'Italy'
historydict['level'] = 'middle'
historydict['level'] = 'senior'

print(historydict.all_history())

del historydict['level']

print(historydict.all_history())

historydict['level'] = 'God'

print(historydict.all_history())
