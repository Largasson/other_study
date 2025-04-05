class LowerString(str):
    def __new__(cls, obj=''):
        return str.__new__(cls)

    def __str__(self):
        return self.lower()

print(LowerString(['Bee', 'Geek']))
print(LowerString({'A': 1, 'B': 2, 'C': 3}))