def is_natural(num):
    for i in range(2, num):
        if num % i == 0:
            return None
    return num


def is_polindrom(num: int):
    if str(num) == str(num)[::-1]:
        return num
    return None


num = 2
num_lst = []
num_poly = []
while len(num_lst) < 1000:
    if isinstance(is_natural(num), int):
        num_lst.append(num)
        if isinstance(is_polindrom(num), int):
            num_poly.append(num)
    num += 1

print(num_lst)
print()
print(num_poly)
print(len(num_poly))

# res = []
# for num in range(0, 2000):
#     res.append(is_polindrom(num))


# print(res)
