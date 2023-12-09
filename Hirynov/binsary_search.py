def bi_serch(lst, item):
    """функция, осуществляющая бинарный поиск элемента в массиве"""
    low = 0
    hight = len(lst) - 1
    while low <= hight:
        position = (low + hight) // 2 # по факту - среднее значение между максимумом и минимумом
        if item == lst[position]:
            return f'Индекс искомого элемента - {position}' # возращаем индекс, в которой находится искомый элемент
        elif item > lst[position]:
            low = position + 1
        elif item < lst[position]:
            hight = position - 1
    return f'Нет такого элемента в списке'

def test(algorithm):
    print('Тестируем:', algorithm.__doc__)
    print('Тест 1: ', end='')
    lst = [1, 3, 5, 7, 9] # список, в котором будем искать элемент
    item = 3 # элемент для поиска
    print(algorithm(lst, item))

    print('Тест 2: ', end='')
    lst = list(range(1, 101)) # список, в котором будем искать элемент
    item = 87 # элемент для поиска
    print(algorithm(lst, item))

    print('Тест 3: ', end='')
    lst = list(range(1, 101))  # список, в котором будем искать элемент
    item = -5  # элемент для поиска
    print(algorithm(lst, item))

if __name__ == "__main__":
    test(bi_serch)
