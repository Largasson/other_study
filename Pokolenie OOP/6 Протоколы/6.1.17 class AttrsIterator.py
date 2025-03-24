class AttrsIterator:
    def __init__(self, obj):
        self.attrs = obj.__dict__
        self.iter = iter(self.attrs.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iter)

class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


user = User('Debbie', 'Harry', 77)
attrsiterator = AttrsIterator(user)

print(*attrsiterator)

print(attrsiterator.attrs)
