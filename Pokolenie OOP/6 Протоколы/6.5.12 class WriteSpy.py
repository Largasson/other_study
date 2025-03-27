class WriteSpy:
    def __init__(self, file1, file2, to_close= False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close

    def __enter__(self):
        return self

    def write(self, text):
        try:
            self.file1.write(text)
            self.file2.write(text)
        except ValueError as err:
            print(f"Файл закрыт или недоступен для записи")

    def close(self):
        self.file1.close()
        self.file2.close()

    def writable(self):
        if self.file1.closed or self.file2.closed:
            return False
        else:
            return self.file1.writable() and self.file2.writable()

    def closed(self):
        return self.file1.closed and self.file2.closed

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.to_close:
            self.file1.close()
            self.file2.close()


# TEST_7:
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')
f1.close()

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.writable())

# TEST_8:
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    pass

print(combined.closed())

# TEST_9:
f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2) as combined:
    pass

print(combined.closed())