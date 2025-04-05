class FieldTracker:

    def __setattr__(self, attr, value):
        if attr not in self.__dict__:
            self.__dict__[attr] = []
        if len(self.__dict__[attr]) > 0 and self.__dict__[attr][-1] == value:
            return
        self.__dict__[attr].append(value)

    def __getattribute__(self, attr):
        # Используем super для безопасного доступа к __dict__
        if attr == "__dict__":  # предотвратить рекурсию
            return super().__getattribute__(attr)
        # Получаем словарь атрибутов через super
        __dict__ = super().__getattribute__("__dict__")
        if attr in __dict__ and __dict__[attr]:  # Если атрибут существует и не пуст
            return __dict__[attr][-1]  # Вернуть последний элемент
        return super().__getattribute__(attr)  # Для остальных случаев


    def base(self, attr):
        if len(self.__dict__[attr]) > 1:
            return self.__dict__[attr][0]
        return self.__dict__[attr][-1]

    def has_changed(self, attr):
        if len(self.__dict__[attr]) > 1:
            return True
        return False

    def changed(self):
        original_attrs = {}
        for attr in self.__dict__:
            if self.has_changed(attr):
                original_attrs[attr] = self.base(attr)
        return original_attrs

    def save(self):
        for attr in self.__dict__:
            if self.has_changed(attr):
                temp = self.__dict__[attr][-1]
                self.__dict__[attr] = [temp]


class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


p = Point(1, 2, 3)
print(p.changed())
p.x = 4
print(p.changed())
print(p.x)
p.z = 6
print(p.changed())
p.save()
print(p.changed())
p.y = 8
print(p.changed())
print(p.y)
p.save()
print(p.changed())
p.save()
print(p.changed())










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
# testing_lesson('21.zip')