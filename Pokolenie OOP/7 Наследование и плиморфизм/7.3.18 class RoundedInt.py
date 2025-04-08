class RoundedInt(int):
    def __new__(cls, value, even=True):
        value += (value % 2 != 0) if even else (value % 2 == 0)
        return super().__new__(cls, value)


roundedint1 = RoundedInt(7)
roundedint2 = RoundedInt(7, False)

print(roundedint1 + roundedint2)
print(roundedint1 + 1)
print(roundedint2 + 1)

print(type(roundedint1))
print(type(roundedint2))
