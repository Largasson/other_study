class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'

class SortKey:
    def __init__(self, *args):
        self.args = list(args)

    def __call__(self, obj):
        return tuple(obj.__dict__[i] for i in self.args)


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20)]

print(sorted(users, key=SortKey('name')))
print(sorted(users, key=SortKey('name', 'age')))