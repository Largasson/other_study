from datetime import date


class WeatherWarning:
    def rain(self, date: date = None):
        if date:
            print(date.strftime("%d.%m.%Y"))
        print("Ожидаются сильные дожди и ливни с грозой")

    def snow(self, date: date = None):
        if date:
            print(date.strftime("%d.%m.%Y"))
        print("Ожидается снег и усиление ветра")

    def low_temperature(self, date: date = None):
        if date:
            print(date.strftime("%d.%m.%Y"))
        print("Ожидается сильное понижение температуры")


class WeatherWarningWithDate(WeatherWarning):
    def rain(self, date: date = None):
        super().rain(date)

    def snow(self, date: date = None):
        super().snow(date)

    def low_temperature(self, date: date = None):
        super().low_temperature(date)




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