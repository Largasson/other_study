class MaxCallsException(Exception):
    def __init__(self):
        message =  "Превышено количество доступных обращений"
        super().__init__(message)

class LimitedTakes:
    def __init__(self, max_take):
        self.max_take = max_take
        self.counter = 0

    def __set_name__(self, owner, attr):
        self._attr = attr

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._attr in instance.__dict__:
            if self.counter < self.max_take:
                self.counter += 1
                return instance.__dict__[self._attr]
            else:
                raise MaxCallsException
        else:
            raise AttributeError("Атрибут не найден")

    def __set__(self, instance, value):
        instance.__dict__[self._attr] = value


class Student:
    name = LimitedTakes(3)


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



testing_lesson('17.zip')