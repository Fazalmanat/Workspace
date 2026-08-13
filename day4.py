#Prime
# import math
# num=int(input("Enter the Number:"))
# if num==2:
#     print("is prime")
# elif num%2==0 or num<=1:
#     print("not prime")
# else:
#     for i in range(3,int(math.sqrt(num)),2):
#         if num%i==0:
#             print("not prime")
#             break
#     else:
#         print("is prime")

#Perfect
# num=int(input("enter the number : "))
# sum=1
# for i in range(2,num//2+1):
#     if num%i==0:
#         sum +=i
# if num==sum:
#     print("is perfect")
# else:
#     print("not perfect")

#Strong
# num=int(input("Enter The Number : "))
# sum=num
# f=1
# while num>0:
#     for i in range(1,num%10 +1):
#         f*=i
#     sum -=f
#     f=1
#     num = num//10
# if sum==0:
#     print("is Strong")
# else:
#     print("not strong")

#Spy
# num=int(input("Enter The Number : "))
# sum=0
# product=1
# while num>0:
    
#     sum += num%10
#     product *= num%10
#     num = num//10
# if sum==product:
#     print("is Spy")
# else:
#     print("not Spy")

#Armstrong
num=int(input("Enter The Number : "))
sum=num
for i in range(num//2+1):
    if num//(10**i)==0:
        break
while num>0:
    sum -= (num%10)**i
    num = num//10
    
if sum==0:
    print("is Armstrong")
else:
    print("not Armstrong")