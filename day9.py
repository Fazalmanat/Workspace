# s="python"
# for i in range(len(s)):
#     print(s[:i+1],end="")
#     print("  "*(len(s)-s.find(s[i])),end="")
#     print(s[i::-1])
    
#vowels
s=input("Enter the String : ")
count=0
for i in s:
    if i in ("a","e","i","o","u"):
        count +=1
print(count)

#count char
# s=input("Enter the String : ")
# print(s.count("")-1)

#upper lower count
# s=input("Enter The String : ")
# upperCount=0
# lowerCount=0
# for i in s:
#     if i.isupper():
#         upperCount+=1
#     elif i.islower():
#         lowerCount+=1
# print(f"No of Uppercase Letters is {upperCount} and No of Lowercase Letters is {lowerCount}.")

#space Count

# s=input("Enter The String : ")
# print(s.count(" "))