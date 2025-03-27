import sys


class UpperPrint:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.fun


    def fun(self, text):
        return self.original_write(text.upper())

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.original_write



print('Если жизнь одаривает вас лимонами — не делайте лимонад')
print('Заставьте жизнь забрать их обратно!')

# Использование контекстного менеджера UpperPrint
with UpperPrint():
    print('Мне не нужны твои проклятые лимоны!')
    print('Что мне с ними делать?')

print('Требуйте встречи с менеджером, отвечающим за жизнь!')
