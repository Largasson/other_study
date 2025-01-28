import re
import sys

regex = r'""".*?"""'
regex2 = r'\n?#.*'

text = ''
for line in sys.stdin:
    text+=line
result1 = re.sub(regex, '', text, flags=re.DOTALL).strip()
result2 = re.sub(regex2, '', result1)
print(result2)
