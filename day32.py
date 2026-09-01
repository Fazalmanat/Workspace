import re
s="The 1rain in 12Espada is 03magical"
# x=re.findall("fill|kill",s)
# print(x)
# x=re.findall("[arn]",s)
# print(x)
# x=re.findall("[A-z]",s)
# x=re.findall("[^is ]",s)
# x=re.findall("[1-9]",s)
# x=re.findall("[0-1][0-3]",s)
x=re.findall("[a-zA-Z]",s)
print(x)