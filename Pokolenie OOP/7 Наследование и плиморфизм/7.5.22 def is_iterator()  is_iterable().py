from collections.abc import Iterable, Iterator

def is_iterator(obj):
   return isinstance(obj, Iterator)

def is_iterable(obj):
   return isinstance(obj, Iterable)



print(is_iterator(123))
print(is_iterator([1, 2, 3]))
print(is_iterator((1, 2, 3)))
print(is_iterator('123'))
print(is_iterator(iter('123')))
print(is_iterator(map(int, '123')))



