import sys

lst = [s for s in sys.stdin]
res = len(lst) - len(set(lst))
print(res)
