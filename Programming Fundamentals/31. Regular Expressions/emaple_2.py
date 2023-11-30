import re

text = 'the year is 2012'
pattern = '\d+'
result = re.findall(pattern, text)
print(result)
