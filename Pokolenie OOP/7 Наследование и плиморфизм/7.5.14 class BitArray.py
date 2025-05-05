from collections.abc import Sequence


class BitArray(Sequence):
    def __init__(self, iterable=None):
        if not iterable:
            self._data = []
        else:
            self._data = iterable.copy()

    def __str__(self):
        return str(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)

    def __invert__(self):
        return BitArray([int(not elem) for elem in self._data])

    def __and__(self, other):
        if not isinstance(other, BitArray):
            return NotImplemented
        elif len(self._data) != len(other._data):
            raise TypeError
        return BitArray([a & b for a, b in zip(self._data, other._data)])

    def __or__(self, other):
        if not isinstance(other, BitArray):
            return NotImplemented
        elif len(self._data) != len(other._data):
            raise TypeError
        return BitArray([a | b for a, b in zip(self._data, other._data)])







def testing_lesson(filename: str):
    '''
    Функция выполняет код из каждого файла в архиве и выводит результат выполнения вашего кода и ожидаемый результат

    filename - если указан с *.zip, то выполняется проверка функций из файла
    '''
    from zipfile import ZipFile
    zip_name = filename if filename.endswith('zip') else filename + '.zip'
    with ZipFile(zip_name) as z:
        length = len(z.namelist()) // 2
        files = [(code, out) for code, out in zip(z.namelist()[::2], z.namelist()[1::2])]
        for file_exec, file_out in files:
            with z.open(name=file_exec) as fi:
                with z.open(name=file_out) as fo:
                    code, out = fi.read().decode(), fo.read().decode()
                    print(f'Тест № {file_exec} из {length}')
                    print(f'\nКод: \n\n{code}\n')
                    print('-' * 10)
                    print('Ваш результат:')
                    try:
                        if filename.endswith('zip'):
                            exec(code)
                        else:
                            exec(compile(filename + '(code)', 'tests', 'exec'))
                        print(f"{'-' * 10}\nОжидаемый результат:\n{out}\n{'*' * 10}")
                    except Exception as e:
                        print(f'{"🚫" * 10}\n"Тест № {file_exec} завершился с `ошибкой "{type(e).__name__}: {e}\n')
                        print(f'Ожидаемый результат: \n{out}\n{"🚫" * 50}"\n')


testing_lesson('24.zip')
