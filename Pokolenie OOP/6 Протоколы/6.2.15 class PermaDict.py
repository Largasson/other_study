class PermaDict:
    def __init__(self, data=None):
        self._dict = dict(data) if data else {}

    def keys(self):
        yield from self._dict.keys()

    def values(self):
        yield from self._dict.values()

    def items(self):
        yield from self._dict.items()

    def __len__(self):
        return len(self._dict)

    def __iter__(self):
        return iter(self._dict.keys())

    def __getitem__(self, item):
        return self._dict[item]

    def __setitem__(self, key, value):
        if key in self._dict:
            raise KeyError("Изменение значения по ключу невозможно")
        self._dict[key] = value

    def __delitem__(self, key):
        del self._dict[key]




# TEST_5:
d = dict.fromkeys(range(100), None)
attrdict = PermaDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)

# TEST_6:
d = {'Ерофей Всеволодович Сидоров': '13.05.1985', 'Семенов Андрон Денисович': '24.03.1988',
     'Петухова Лукия Максимовна': '15.06.1993', 'Лидия Георгиевна Фадеева': '25.12.1980',
     'Федотова Надежда Юрьевна': '04.06.1992', 'Харитонов Варфоломей Марсович': '14.06.1994',
     'Глафира Феликсовна Фомина': '29.08.1984', 'Пелагея Николаевна Брагина': '01.04.1986',
     'Никита Ильясович Макаров': '29.08.1992', 'Лихачева Майя Алексеевна': '12.11.1991',
     'Виноградова Нина Олеговна': '07.08.1992', 'Артемьева Кира Валентиновна': '11.04.1997',
     'Василиса Федоровна Уварова': '03.05.1981', 'Денисов Варфоломей Устинович': '17.04.1990',
     'Тихонова Клавдия Филипповна': '18.11.1988', 'Зимина Любовь Викторовна': '23.06.1983',
     'Кудряшов Викторин Фомич': '27.06.1997', 'Юлия Вениаминовна Ефимова': '20.10.1987',
     'Никандр Валерианович Мельников': '10.02.1985', 'Устинова Лидия Артемовна': '30.06.1992'}

permadict = PermaDict(d)

for key in permadict.keys():
    print(key, end='; ')

print('\n')

for value in permadict.values():
    print(value, end='; ')

print('\n')

for item in permadict.items():
    print(item, end='; ')

# TEST_7:
permadict = PermaDict()
print('Keys:', *permadict.keys())
print('Values:', *permadict.values())
print('Items:', *permadict.items())