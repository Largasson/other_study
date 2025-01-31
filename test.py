n = int(input())
lst = [[0 for i in range(n)] for _ in range(n)]

for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst[i][j] = min(i, j, n - i - 1, n - j - 1) + 1

for row in range(len(lst)):
    print(' '.join(map(str, lst[row])))
