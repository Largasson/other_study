import keyword

class NonKeyword:
    def __init__(self, attr):
        self._attr = attr

    def __get__(self, instance, cls):
        if instance is None:
            return self
        try:
            return instance.__dict__[self._attr]
        except KeyError:
            raise AttributeError(f'Атрибут не найден')

    def __set__(self, instance, value):
        if value in keyword.kwlist:
            raise ValueError('Некорректное значение')
        instance.__dict__[self._attr] = value



# TEST_4:
class Student:
    name = NonKeyword('name')

student = Student()

try:
    student.name = 'class'
except ValueError as e:
    print(e)

# TEST_5:
from keyword import kwlist

class Student:
    name = NonKeyword('name')

student = Student()

for kw in kwlist:
    try:
        student.name = kw
    except ValueError as e:
        print(e)

# TEST_6:
class NonKeywordData:
    obj = NonKeyword('obj')


data = [1, 2.3, [4, 5, 6], (7, 8, 9), {10: 11, 12: 13, 14: 15}, True, False, 'Mantrida']
nonkeyworddata = NonKeywordData()

for item in data:
    nonkeyworddata.obj = item
    print(nonkeyworddata.obj)

# TEST_7:
class Student:
    name = NonKeyword('name')

print(Student.name.__class__)