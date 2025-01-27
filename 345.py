import re
import sys

regex = r'beegeek'
count = 0
for elem in sys.stdin:
    if re.search(regex, elem, re.IGNORECASE):
        count += 1
print(count)
