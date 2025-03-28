import sys
from contextlib import contextmanager

@contextmanager
def reversed_print():
    standart_out_write = sys.stdout.write
    sys.stdout.write = lambda text: standart_out_write(text[::-1])
    yield
    sys.stdout.write = standart_out_write

print('Вывод вне блока with')

with reversed_print():
    print('Вывод внутри блока with')

print('Вывод вне блока with')