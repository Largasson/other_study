objects = [1,2,3,4,5,11,1,1,1,2,3,12,3]
ans = 0
lst = []
for obj in objects: # доступная переменная objects
    if obj not in lst:
        lst.append(obj)
        ans += 1

print(ans)