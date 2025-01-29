from re import sub


def func(match_obj):
    word = match_obj.group(0)
    temp = word[:2]
    s = temp[::-1]
    res = s+word[2:]
    return res
text = input()
result = sub(r'\w+', func, text)

print(result)
