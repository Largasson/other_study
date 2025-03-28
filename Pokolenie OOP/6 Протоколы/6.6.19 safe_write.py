from contextlib import contextmanager


@contextmanager
def safe_write(filename):
    try:
        open_file = open(filename, 'r+', encoding='utf-8')
        temp_data = open_file.read()
        open_file.seek(0)
    except FileNotFoundError:
        open_file = open(filename, 'w', encoding='utf-8')
        temp_data = ''

    try:
        yield open_file
    except Exception as e:
        print(f'Во время записи в файл было возбуждено исключение {type(e).__name__}')
        open_file.seek(0)
        open_file.write(temp_data)
        open_file.truncate()
    finally:
        open_file.close()




with safe_write('under_tale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')

with safe_write('under_tale.txt') as file:
    print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file, flush=True)
    raise ValueError

with open('under_tale.txt') as file:
    print(file.read())