class ReversibleString:
    def __init__(self, string: str):
        self.string = string

    def __str__(self):
        return f"{self.string}"

    def __neg__(self):
        return ReversibleString(self.string[::-1])

string = ReversibleString('beegeek')

print(-string)
print(type(-string))