class PositiveNumber:
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        return getattr(obj, self._attr)

    def __set__(self, obj, value):
        if type(value) in (int, float) and value > 0:
            setattr(obj, self._attr, value)
        else:
            raise ValueError('Некорректное значение')

class Cat:
    age = PositiveNumber()

    def __init__(self, age):
        self.age = age


cat = Cat(1)

print(cat.age)