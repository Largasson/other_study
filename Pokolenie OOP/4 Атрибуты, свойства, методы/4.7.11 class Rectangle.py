class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.a = b
        self.a = c

    @classmethod
    def from_iterable(cls,*args):
        return cls(args[0], args[1], args[2])

    @classmethod
    def from_str(cls,string):
        a, b, c = list(map(float, string.split()))
        return cls(a, b, c)

polynom = QuadraticPolynomial(1, -5, 6)

print(polynom.a)
print(polynom.b)
print(polynom.c)

