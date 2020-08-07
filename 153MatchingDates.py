import re
str1 ="12-3-2020 and 11-3-2000 "

result = re.findall(r'\d{1,2}-\d{1,2]-\d{4}',str1)
print(result)