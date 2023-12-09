from functools import singledispatchmethod

class BirthInfo:
    def __init__(self, birth_date):
        pass


    @singledispatchmethod
    @staticmethod
    def format(arg):
        raise TypeError('Аргумент переданного типа не поддерживается')

