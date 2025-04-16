from abc import ABC, abstractmethod


class Validator(ABC):
    """Класс дескриптор"""

    @abstractmethod
    def validate(self, value):
        pass

    def __set_name__(self, owner, attr):
        self._attr = attr

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._attr not in instance.__dict__:
            raise AttributeError('Атрибут не найден')
        return instance.__dict__[self._attr]

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self._attr] = value


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Устанавливаемое значение должно быть числом')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
        elif self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')


class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate: callable(str) = None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError('Устанавливаемое значение должно быть строкой')
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
        elif self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
        elif self.predicate is not None and not self.predicate(value):
            raise ValueError('Устанавливаемая строка не удовлетворяет дополнительным условиям')


# TEST_16:
class Student:
    age = Number(18, 99)


student = Student()
try:
    print(student.age)
except AttributeError as e:
    print(e)


# TEST_17:
class Student:
    age = Number(18, 99)


print(Student.age.__class__)
