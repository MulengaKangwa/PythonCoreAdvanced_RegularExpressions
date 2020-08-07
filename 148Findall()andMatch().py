import re
str ="Take up one idea.One idea at a time"

result = re.search(r'o\w\w',str)
print(result.group()) #This will return none if the search does not apply.

result = re.findall(r'O\w\w',str)
print(result)

result = re.match(r'T\w\w',str)
print(result.group())