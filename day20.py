#1 pythagorean triplets
# import math
# li=[1,2,3,4,5,1.414]
# for i in range(len(li)):
#     for j in li[i:]:
#         h=math.sqrt((li[i]**2)+(j**2))
#         if h in li:
#             print(li[i],j,h)
            
#2twin_prime
# def is_prime(num):
#     import math
#     if(num==2):
#         return True
#     elif num%2==0 or num<=1:
#         return False
#     else:
#         for i in range(3,int(math.sqrt(num))+1,2):
#             if num%i==0:
#                 return False
#         else:
#             return True
# li=[1,2,5,3,11,13]
# r=[]
# for i in li:
#     if is_prime(i):
#         if i+2 in li and is_prime(i+2):
#             if (i,i+2) and (i+2,i)not in r:
#                 r.append((i,i+2))
#         if i-2 in li and is_prime(i-2):
#             if (i,i-2) and (i-2,i) not in r:
#                 r.append((i,i-2))
# print(r)

#3 even as sum of 2 prime
# num=int(input("Enter even number : "))
# for i in range(2,num//2+1):
#     if is_prime(i) and is_prime(num-i):
#         print(i,num-i)

#4 divisible by sum
# for num in range(1,21):
#     s=0
#     n=num
#     while(n>0):
#         s+=n%10
#         n//=10
#     if num%s==0:
#         print(num,True)
#     else:
#         print(num,False)

#5group into prime,composite,perfect,armstrong,palindrome,even,odd
# def is_arm(num):
#     sum=num
#     for i in range(num//2+1):
#         if num//(10**i)==0:
#             break
#     while num>0:
#         sum -= (num%10)**i
#         num = num//10
    
#     if sum==0:
#         return True
#     else:
#         return False
    
# def is_perf(num):
#     sum=1
#     for i in range(2,num//2+1):
#         if num%i==0:
#             sum +=i
#     if num==sum:
#         return True
#     else:
#         return False
    
# def is_pal(num):
#     r=0
#     n=num
#     while(n>0):
#         r=(r*10)+(n%10)
#         n=n//10
#     if r==num:
#         return True
#     else:
#         return False
            
# dict1={"prime":[],"comp":[],"perf":[],"arms":[],"pal":[],"even":[],"odd":[]}
# li=[158,212,39,40]
# for i in li:
#     if is_prime(i):
#         dict1["prime"].append(i)
#     else:
#         if i>2:
#             dict1["comp"].append(i)
#     if is_perf(i):
#         dict1["perf"].append(i)
#     if is_arm(i):
#         dict1["arms"].append(i)
#     if is_pal(i):
#         dict1["pal"].append(i)
#     if i%2==0:
#         dict1["even"].append(i)
#     else:
#         dict1["odd"].append(i)
# print(dict1)

#6 neon
# num=int(input("enter the number : "))
# s=0
# n=num**2
# while(n>0):
#     s+=n%10
#     n//=10
# if s==num:
#     print("Neon")
# else:
#     print("Not Neon")