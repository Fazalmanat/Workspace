# import math
# num=int(input("Enter your Number :"))
# if(num==2):
#     print("is prime")
# elif num%2==0 or num<=1:
#     print("not prime")
# else:
#     for i in range(3,int(math.sqrt(num)),2):
#         if num%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")

#Sum Of Natural Numbers
# num=int(input("Enter the number of Terms: "))
# sum=0
# for i in range(1,num+1):
#     sum += i
# print(sum)

#Multiplication table
# num=int(input("enter the number :"))
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")

#All even numbers between 1 and 50
# for i in range(1,50):
#     if i%2==0:
#         print(i) 

#sum of digits
num=int(input("Enter the number : "))
sum=0
i=1
while num>0:
    sum+=num%10
    num=num//10
    i+=1
print(sum)




# sum=0
# while(True):
#     num=int(input("Enter the number :"))
#     if num==0:
#         break
#     else:
#         sum += num
# print(sum)

