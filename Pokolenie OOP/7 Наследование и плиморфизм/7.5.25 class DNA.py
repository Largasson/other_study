from collections.abc import Sequence, Iterable

class DNA(Sequence):
    the_dict = {
        "T": "A",
        "A": "T",
        "G": "C",
        "C": "G"
    }

    def __init__(self, chain):
        self.chain = chain
        self._dna = []
        for ch in chain:
            self._dna.append((ch, self.the_dict[ch]))

    def __repr__(self):
        return self.chain

    def __len__(self):
        return len(self.chain)

    def __reversed__(self):
        return self._dna[::-1]

    def __getitem__(self, key):
        return self._dna[key]

    def __contains__(self, item):
        return item in self.chain

    def __eq__(self, other):
        if not isinstance(other, DNA):
            return NotImplemented
        return self.chain == other.chain

    def __add__(self, other):
        if not isinstance(other, DNA):
            return NotImplemented
        return DNA(self.chain + other.chain)

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



testing_lesson('25.zip')