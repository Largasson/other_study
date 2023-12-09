lst = input().split()
num = int(input())
a = 0
res = []
l = lst.count(str(num))
for _ in range(l):
    a = lst.index(str(num), a, len(lst))
    res.append(a)
    a += 1
if res == []:
    print(None)
else:
    print(*res)


