#1_common elements
# list1=input("Enter List 1 : ").split(" ")
# list2=input("Enter List 2 : ").split(" ")
# for i in list1:
#     if i in list2:
#         print(i)

#2 Remove Duplicates
# list1=input("enter the list : ").split(" ")
# for i in list1:
#     if list1.count(i)>1:
#         list1.remove(i)
# print(list1)

#3reverse without using reverse
# list1=input("Enter the List : ").split(" ")
# print(list1[::-1])

#4 count odd and even
# List1=(input("enter the List : ")).split(" ")
# odd=0
# even=0
# for i in List1:
#     if int(i)%2==0:
#         even+=1
#     else:
#         odd+=1
# print("odd : ",odd," even : ",even)

#6find sum without sum()
# List1=input("Enter The List : ").split(" ")
# sum=0
# for i in List1:
#     sum+=int(i)
# print(sum)

#7count positive and negative
# List1=input("Enter the List : ").split(" ")
# pos=0
# neg=0
# for i in List1:
#     if int(i)>0:
#         pos+=1
#     elif int(i)<0:
#         neg+=1
# print(f"positive : {pos} and negative : {neg}")

#8 average 
# List1=input("Enter the List : ").split()
# sum=0
# for i in List1:
#     sum+=int(i)
# print(sum/len(List1))

#9 Count frequency
# List1=input("Enter the List :").split(" ")
# char=input("Enter the character : ")
# print(List1.count(char))

#10 all values greater than average
# List1=input("Enter The List : ").split(" ")
# List1=[int(x) for x in List1]
# List1.sort()
# avg=0
# for i in List1:
#     avg+=i
# avg=avg/len(List1)
# for j in range(len(List1)):
#     if List1[j]>avg:
#         print(List1[j:])
#         break

#11 move all zeros to end while non zero order no change
# List1=input("Enter the String : ").split(" ")
# List1=[int(x) for x in List1]
# for i in List1:
#     if i==0:
#         List1.remove(0)
#         List1.append(0)
# print(List1)
