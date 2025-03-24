class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        if self.b ** 2 - (4 * self.a * self.c) < 0:
            return None
        return (- self.b - (self.b ** 2 - (4 * self.a * self.c)) ** 0.5) / (2 * self.a)

    @property
    def x2(self):
        if self.b ** 2 - (4 * self.a * self.c) < 0:
            return None
        return (- self.b + (self.b ** 2 - (4 * self.a * self.c)) ** 0.5) / (2 * self.a)

    @property
    def view(self):
        return f'{self.a}x^2 + {self.b}x + {self.c}'.replace('+ -', '- ')

    @property
    def coefficients(self):
        return (self.a, self.b, self.c)

    @coefficients.setter
    def coefficients(self, coefficients):
        self.a, self.b, self.c = coefficients


# INPUT DATA:

# TEST_1:
polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.a)
print(polynom.b)
print(polynom.c)

# TEST_2:
polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.x1)
print(polynom.x2)

# TEST_3:
polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.view)
print(polynom.coefficients)

# TEST_4:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 6)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_5:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 0)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_6:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, 0, -9)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_7:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (5, 0, 0)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_8:
polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()

polynom.coefficients = (-1000, 1202, -202)
print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

# TEST_9:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (5, 3, 1)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)