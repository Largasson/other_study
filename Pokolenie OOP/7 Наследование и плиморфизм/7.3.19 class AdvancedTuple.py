from collections.abc import Iterable


class AdvancedTuple(tuple):
    def __add__(self, other):
        if isinstance(other, Iterable):
            if isinstance(other, dict):
                return AdvancedTuple(tuple(self) + tuple(other.keys()))
            return AdvancedTuple(tuple(self) + tuple(other))
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Iterable):
            if isinstance(other, dict):
                return AdvancedTuple(tuple(other.keys()) + tuple(self))
            return AdvancedTuple(tuple(other) + tuple(self))
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Iterable):
            if isinstance(other, dict):
                return AdvancedTuple(tuple(self) + tuple(other.keys()))
            return AdvancedTuple(tuple(self) + tuple(other))
        return NotImplemented


advancedtuple = AdvancedTuple([1, 2, 3])

not_supported = [1, 1.0, None]

for item in not_supported:
    try:
        advancedtuple = advancedtuple + item
    except TypeError as e:
        print(e)

#
# def testing_lesson(filename: str):
#     '''
#     Функция выполняет код из каждого файла в архиве и выводит результат выполнения вашего кода и ожидаемый результат
#
#     filename - если указан с *.zip, то выполняется проверка функций из файла
#     '''
#     from zipfile import ZipFile
#     zip_name = filename if filename.endswith('zip') else filename+'.zip'
#     with ZipFile(zip_name) as z:
#         length = len(z.namelist()) // 2
#         files = [(code, out) for code, out in zip(z.namelist()[::2], z.namelist()[1::2])]
#         for file_exec, file_out in files:
#             with z.open(name=file_exec) as fi:
#                 with z.open(name=file_out) as fo:
#                     code, out = fi.read().decode(), fo.read().decode()
#                     print(f'Тест № {file_exec} из {length}')
#                     print(f'\nКод: \n\n{code}\n')
#                     print('-' * 10)
#                     print('Ваш результат:')
#                     try:
#                         if filename.endswith('zip'):
#                             exec(code)
#                         else:
#                             exec(compile(filename + '(code)', 'tests', 'exec'))
#                         print(f"{'-' * 10}\nОжидаемый результат:\n{out}\n{'*' * 10}")
#                     except Exception as e:
#                         print(f'{"🚫" * 10}\n"Тест № {file_exec} завершился с `ошибкой "{type(e).__name__}: {e}\n')
#                         print(f'Ожидаемый результат: \n{out}\n{"🚫" * 50}"\n')
#
#
#
# testing_lesson('19.zip')
