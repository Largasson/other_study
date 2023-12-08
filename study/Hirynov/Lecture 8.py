def marge(a: list, b: list):    # функция слияния
    c = [0] * (len(a) + len(b))
    i = j = k = 0


    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c[k] = a[i]
            i += 1
            k += 1
        else:
            c[k] = b[j]
            j += 1
            k += 1
    while i < len(a):
        c[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        c[k] = b[j]
        j += 1
        k += 1
    return c


def recursive_marge_sort(lst: list):           # функция сортировки
    if len(lst) < 2:
        return
    middle = len(lst) // 2
    left = [i for i in lst[:middle]]
    right = [i for i in lst[middle:]]
    recursive_marge_sort(left)
    recursive_marge_sort(right)
    sort_lst = marge(left, right)
    for i in range(len(lst)):
        lst[i] = sort_lst[i]


m = [5, 8, 7, 4, 2, -78, -12, -9, 1, 5, 3, -100]
recursive_marge_sort(m)
print(m)
