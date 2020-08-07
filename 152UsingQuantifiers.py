import re
str ="Take up One idea.One idea at a time"

result = re.findall(r'O\w+',str)
print(result)

result = re.findall(r'O\w?',str)
print(result)

result = re.findall(r'O\w{2}',str)
print(result)

result = re.findall(r'O\w{1,2}',str)
print(result)

