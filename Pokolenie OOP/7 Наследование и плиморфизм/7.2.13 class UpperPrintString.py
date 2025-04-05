class UpperPrintString(str):
    def __str__(self):
        return self.upper()

s1 = UpperPrintString('beegeek')
s2 = UpperPrintString('BeeGeek')

print(s1)
print(s2)