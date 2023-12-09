from functools import singledispatchmethod

class Negator:

    @singledispatchmethod
    @staticmethod
    def neg(arg):
        raise TypeError('Аргумент переданного типа не поддерживается')


    @neg.register(int|float)
    @staticmethod
    def _neg(arg):
        return -arg

    @neg.register(bool)
    @staticmethod
    def _neg(arg):
        if arg is True:
            return False
        return True

print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))

try:
    Negator.neg('number')
except TypeError as e:
    print(e)

