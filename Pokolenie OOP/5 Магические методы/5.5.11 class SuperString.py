class SuperString:
    def __init__(self, string: str):
        self.string = string

    def __str__(self):
        return f"{self.string}"

    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return SuperString(self.string * other)
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return SuperString(self.string * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int):
            return SuperString(self.string[:((len(self.string)) // other)])
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            return SuperString(self.string[other:])
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            return SuperString(self.string[:-other if other > 0 else len(self.string)+1])
        return NotImplemented


# # TEST_4:
# s = SuperString('beegeek')
# for i in range(9):
#     print(f'{s} << {i} =', s << i)
#


s = SuperString('beegeek')
s << 0
print(s << 1)