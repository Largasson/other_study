from collections import UserDict

class LowerCaseDict(UserDict):
    def __setitem__(self, key, value):
        key = str(key).lower()
        super().__setitem__(key, value)


lowercasedict  = LowerCaseDict({'ONE': 1})
lowercasedict['TWO'] = 2
lowercasedict.update({'THREE': 3})

print(lowercasedict)