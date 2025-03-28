from contextlib import contextmanager


@contextmanager
def make_tag(tag):
    print(tag)
    yield
    print(tag)

with make_tag('---'):
    print('Поколение Python')