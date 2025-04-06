class TitledText(str):
    def __new__(cls, text, title):
        instance = super().__new__(cls, text)
        instance._title = title
        return instance

    def title(self):
        return self._title

titled = TitledText('Сreate a class Soda', 'Homework')

print(titled)
print(titled.title())
print(issubclass(TitledText, str))