from copy import deepcopy, copy


class Atomic:
    def __init__(self, data, deep=False):
        self.data = data
        self.deep = deep

    def __enter__(self):
        self.original_data = deepcopy(self.data) if self.deep else copy(self.data)
        return self.data

    def deep_update(self, original_data):
        if isinstance(self.data, list):
            self.data.clear()
            self.data.extend(original_data)
        elif isinstance(self.data, dict):
            self.data.clear()
            self.data.update(original_data)
        elif isinstance(self.data, set):
            self.data.clear()
            self.data.update(original_data)

    def updete(self, original_data):
        if isinstance(self.data, list):
            for i in range(len(self.original_data)):
                self.data[i] = self.original_data[i]
            del self.data[len(self.original_data):]
        elif isinstance(self.data, dict):
            for key in self.original_data.keys():
                self.data[key] = self.original_data[key]
        elif isinstance(self.data, set):
            self.data.clear()
            self.data.update(original_data)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            if self.deep:
                self.deep_update(self.original_data)
            else:
                self.updete(self.original_data)
        return True


# TEST_1:
numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[1]

print(numbers)

# TEST_2:
numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[100]           # обращение по несуществующему индексу

print(numbers)

# TEST_3:
matrix = [[1, 2], [3, 4]]

with Atomic(matrix) as atomic:
    atomic[1].append(0)       # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]           # обращение по несуществующему индексу

print(matrix)

# TEST_4:
matrix = [[1, 2], [3, 4]]

with Atomic(matrix, True) as atomic:
    atomic[1].append(0)       # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]           # обращение по несуществующему индексу

print(matrix)

# TEST_5:
numbers = {1, 2, 3, 4, 5}

with Atomic(numbers) as atomic:
    atomic.add(6)
    atomic.append(7)           # добавление элемента с помощью несуществующего метода

print(sorted(numbers))

with Atomic(numbers) as atomic:
    atomic.add(6)

print(sorted(numbers))

# TEST_6:
data = {'firstname': 'Alyson', 'lastname': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}

with Atomic(data, True) as atomic:          # deep = True
    atomic['birthday']['month'] = 'April'   # изменение вложенной структуры
    print(atomic['name'])                   # обращение по несуществующему ключу

print(data)

with Atomic(data) as atomic:                # deep = False
    atomic['birthday']['month'] = 'April'   # изменение вложенной структуры
    print(atomic['name'])                   # обращение по несуществующему ключу

print(data)

# TEST_7:
data = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}

with Atomic(data) as atomic:
    atomic['e'] += 2   # изменение структуры

print(data)

# TEST_8:
matrix = [[1, 2], [3, 4]]

with Atomic(matrix, True) as atomic:
    atomic[1].append(0)

print(matrix)