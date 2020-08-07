import re
str ="Take 1 up one 23 idea.One idea 45 at a time"

result = re.search(r'o\w\w',str)
print(result.group()) #This will return none if the search does not apply.

result = re.findall(r'O\w\w',str)
print(result)

result = re.match(r'T\w\w',str)
print(result.group())

result = re.split(r'\d+',str)
print(result)