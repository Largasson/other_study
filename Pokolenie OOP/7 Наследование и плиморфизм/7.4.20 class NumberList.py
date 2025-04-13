from collections import UserList


class NumberList(UserList):
    def __init__(self, iterable=None):
        if iterable is None:
            self.data = []
        else:
            self.data = list(iterable)

        if not all(isinstance(x, (int, float)) for x in self.data):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        super().__init__(iterable)

    @staticmethod
    def num_checker(value):
        if not isinstance(value, (int, float)):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        return True

    def __setitem__(self, index, value):
        NumberList.num_checker(value)
        self.data[index] = value

    def append(self, value):
        NumberList.num_checker(value)
        return super().append(value)

    def extend(self, iterable):
        if not all(isinstance(x, (int, float)) for x in iterable):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        return super().extend(iterable)

    def insert(self, index, value):
        NumberList.num_checker(value)
        return super().insert(index, value)

    def __iadd__(self, other):
        self.extend(other)
        return self


def testing_lesson(filename: str):
    '''
    Функция выполняет код из каждого файла в архиве и выводит результат выполнения вашего кода и ожидаемый результат

    filename - если указан с *.zip, то выполняется проверка функций из файла
    '''
    from zipfile import ZipFile
    zip_name = filename if filename.endswith('zip') else filename+'.zip'
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



testing_lesson('20.zip')