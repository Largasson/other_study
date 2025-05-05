from abc import ABC, abstractmethod


class Stat(ABC):
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        self._num_list = iterable

    def add(self, num):
        self._num_list.append(num)

    def clear(self):
        self._num_list.clear()

    @abstractmethod
    def result(self):
        return NotImplemented


class MinStat(Stat):
    def result(self):
        if self._num_list:
            return min(self._num_list)
        else:
            return None


class MaxStat(Stat):
    def result(self):
        if self._num_list:
            return max(self._num_list)
        else:
            return None


class AverageStat(Stat):
    def result(self):
        return sum(self._num_list) / len(self._num_list) if self._num_list else None


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


testing_lesson('12.zip')
