from abc import ABC, abstractmethod


class CountryDate(ABC):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def iso_format(self):
        return f'{self.year:}-{self.month:02}-{self.day:02}'

    @abstractmethod
    def format(self):
        return NotImplemented


class USADate(CountryDate):
    def format(self):
        return f'{self.month:02}-{self.day:02}-{self.year}'


class ItalianDate(CountryDate):
    def format(self):
        return f'{self.day:02}/{self.month:02}/{self.year}'


italiandate = ItalianDate(2023, 4, 6)

print(italiandate.format())
print(italiandate.iso_format())
