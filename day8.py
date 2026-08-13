# num = int(input("enter the no of rows :"))
# for i in range(1,num+1):
#     if i<=1:
#         pass
#     else:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print("* ",end="")
#     print("* "*i)

l = int(input("enter length of rectangle"))
b = int(input("enter breadth of rectangle"))
for i in range(l):
    if i==0 or i==l-1:
        print("*    "*b+"\n")
    else:
        print("*    "+"     "*(b-2)+"*"+"\n")