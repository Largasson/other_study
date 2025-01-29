from collections import namedtuple
from itertools import combinations

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

max_mass = int(input())
if max_mass < min(iter.mass for iter in items):
    print('Рюкзак собрать не удастся')
else:
    best_value = 0
    best_combination = 0
    acceptable_items = [item for item in items if item.mass <= max_mass]
    for k in range(1, len(acceptable_items) + 1):
        for combination in combinations(acceptable_items, k):
            total_mass = sum(item.mass for item in combination)
            total_price = sum(item.price for item in combination)

            if total_mass <= max_mass and total_price > best_value:
                best_value = total_price
                best_combination = combination
    for item in sorted(best_combination, key=lambda item: item.name):
        print(item.name)
