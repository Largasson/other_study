import re

a, b = map(int, input().split())
string = input()
regex_obj = re.compile(r'\d+')
result = regex_obj.findall(string, pos=a, endpos=b)
print(sum(map(int, result)) if result else 0)

# но я же тут вносил изменения