def summ(l: list):
    if len(l) == 1:
        return l[0]
    x = l.pop()
    return x + summ(l)


def count(l: list):
    if l == []:
        return 0
    return 1 + count(l[1:])


def maxx(l: list, m=0):
    if len(l) == 1:
        return max(m, l[0])
    if l[-1] > m:
        m = l[-1]
        l.pop()
    else:
        l.pop()
    return maxx(l, m)


c = 0


def bin_rec(l: list, z: int, pos=0):
    global c
    c += 1
    if l[pos - 1] == z:
        return l[pos - 1], c
    pos = (len(l)) // 2 - 1
    if z < l[pos]:
        return bin_rec(l[:pos + 1], z, pos)
    else:
        return bin_rec(l[pos:], z, pos)


def quicksort(l):
    if len(l) < 2:
        return l
    pivot = l[0]
    less = [i for i in l[1:] if i >= pivot]
    more = [i for i in l[1:] if i < pivot]
    return quicksort(less) + [pivot] + quicksort(more)


print(quicksort([8, 5, 6, 4, -8, 2, 6, 4, -12, 88, 3, 0]))
