class FuzzyString(str):
    def __eq__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return NotImplemented
        return self.lower() == other.lower()

    def __ne__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return NotImplemented
        return not self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return NotImplemented
        return self.lower() > other.lower()

    def __lt__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return NotImplemented
        return self.lower() < other.lower()

    def __ge__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return NotImplemented
        return self.lower() >= other.lower()

    def __le__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return NotImplemented
        return self.lower() <= other.lower()


    def __contains__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return NotImplemented
        return other.lower() in self.lower()



s = FuzzyString('patrick')

words = ['patrick', 'Patrick', 'pAtrick', 'PAtrick', 'paTrick', 'PaTrick', 'pATrick', 'PATrick', 'patRick', 'PatRick',
         'pAtRick', 'PAtRick', 'paTRick', 'PaTRick', 'pATRick', 'PATRick', 'patrIck', 'PatrIck', 'pAtrIck', 'PAtrIck',
         'paTrIck', 'PaTrIck', 'pATrIck', 'PATrIck', 'patRIck', 'PatRIck', 'pAtRIck', 'PAtRIck', 'paTRIck', 'PaTRIck',
         'pATRIck', 'PATRIck', 'patriCk', 'PatriCk', 'pAtriCk', 'PAtriCk', 'paTriCk', 'PaTriCk', 'pATriCk', 'PATriCk',
         'patRiCk', 'PatRiCk', 'pAtRiCk', 'PAtRiCk', 'paTRiCk', 'PaTRiCk', 'pATRiCk', 'PATRiCk', 'patrICk', 'PatrICk',
         'pAtrICk', 'PAtrICk', 'paTrICk', 'PaTrICk', 'pATrICk', 'PATrICk', 'patRICk', 'PatRICk', 'pAtRICk', 'PAtRICk',
         'paTRICk', 'PaTRICk', 'pATRICk', 'PATRICk', 'patricK', 'PatricK', 'pAtricK', 'PAtricK', 'paTricK', 'PaTricK',
         'pATricK', 'PATricK', 'patRicK', 'PatRicK', 'pAtRicK', 'PAtRicK', 'paTRicK', 'PaTRicK', 'pATRicK', 'PATRicK',
         'patrIcK', 'PatrIcK', 'pAtrIcK', 'PAtrIcK', 'paTrIcK', 'PaTrIcK', 'pATrIcK', 'PATrIcK', 'patRIcK', 'PatRIcK',
         'pAtRIcK', 'PAtRIcK', 'paTRIcK', 'PaTRIcK', 'pATRIcK', 'PATRIcK', 'patriCK', 'PatriCK', 'pAtriCK', 'PAtriCK',
         'paTriCK', 'PaTriCK', 'pATriCK', 'PATriCK', 'patRiCK', 'PatRiCK', 'pAtRiCK', 'PAtRiCK', 'paTRiCK', 'PaTRiCK',
         'pATRiCK', 'PATRiCK', 'patrICK', 'PatrICK', 'pAtrICK', 'PAtrICK', 'paTrICK', 'PaTrICK', 'pATrICK', 'PATrICK',
         'patRICK', 'PatRICK', 'pAtRICK', 'PAtRICK', 'paTRICK', 'PaTRICK', 'pATRICK', 'PATRICK']

print(all(s == item for item in words))




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
# testing_lesson('15.zip')