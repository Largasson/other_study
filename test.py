non_zero = filter(None, [-2, -1, 0, 1, 2])
positive = map(abs, non_zero)

print(list(non_zero))
print(list(positive))