import re
s="this is this"
# print(re.findall("in",s))
# x=re.search("ai",s)
# print(x.start())
# print(re.split('\s',s))
# print(re.sub("this","that",s))
# print(re.findall("t..s",s))
# print(re.findall("^this",s))
print(re.findall("t.*t",s))