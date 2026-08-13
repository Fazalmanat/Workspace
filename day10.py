# #1_first and last 2
# s=input("Enter The String : ")
# if len(s)>1:
#     print("".join(s[:2]+s[-2:]))

#2_ing or ly
# s=input("Enter The String : ")
# if len(s)>=3:
#     if s[-3:]=="ing":
#         s+="ly"
#     else:
#         s+="ing"
# print(s)

# 3_longest word and length from a list of words
s=input("Enter The String : ")
lar_len=0
start=""
for i in s.split(" "):
        if len(i)>lar_len:
            lar_len=len(i)
            start=i
print("Largest Word : "+start+"\nLength:",lar_len)

#4_first char
# s=input("Enter the String : ")
# s=s[0]+s[1:].replace(s[0],"$")
# print(s)

#5_4 copies of last two
# s=input("Enter the String : ")
# print(s[-2:]*4)

#6_reverse if multiple of 4
# s=input("Enter the String : ")
# if len(s)%4==0:
#     print(s[::-1])
# else:
#     print(s)

#7_only alpha
# s=input(":Enter the String : ")
# print(s.isalpha())

#8_only unique
# s=input("Enter the String : ")
# unique=""
# for i in s:
#     if s.count(i)==1:
#         unique+= i
# print(unique)

#9_first repeating
# s=input("Enter The String : ")
# for i in s:
#     if s.count(i)>1:
#         print(i)
#         break

#10_occurrences
# word=input("Enter The Word : ")
# char=input("Enter The Character :")
# print(word.count(char))