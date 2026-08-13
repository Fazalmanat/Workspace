# list1=["apple","kiwi","apple","orange","pineapple"]
# most_occur=""
# # for i in list1:
# #     if list1.count(i)>list1.count(most_occur):
# #         most_occur=i
# print(most_occur)

# li=[x for x in range(1,50) if x%2==0]
# print(li)
# tu=tuple(li)
# print(tu)
# lis=list(tu)
# lis.append("end")
# tu=tuple(lis)
# print(tu)

#1 specified size
# list1=['python','list','exercises','practice','solution']
# result=[x for x in list1 if len(x)==8]
# print(result)

#2 average of two lists
# list1=[1, 1, 3, 4, 4, 5, 6, 7]
# list2=[0, 1, 2, 3, 4, 4, 5, 7, 8]
# list3=list1+list2
# sum=0
# for i in list3:
#     sum+=i
# print(sum/len(list3))

#3 check if sorted
# og_tuple=(1, 4, 2, 6, 8, 10, 12, 14, 16, 17)
# li=list(og_tuple)
# li.sort()
# new_tuple=tuple(li)
# print(og_tuple==new_tuple)

#4 unique_product
# og_tuple=(10, 20, 30, 40, 20, 50, 60, 40)
# product=1
# li=[]
# for i in og_tuple:
#     if i not in li:
#         li.append(i)
#         product*=i
# print(product)

#5 add to string
# tuple1 = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
# s=""
# for i in tuple1:
#     s+=i
# print(s)

#6 avg of tuple in tuples
# Og_Tuple=((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
# average=[]
# avg=0
# for i in range(len(Og_Tuple)):
#     for j in Og_Tuple[i]:
#         avg+=j
#     avg/=len(Og_Tuple[i])
#     average.append(avg)
#     avg=0
# print(average)

#7 replace last value
# li=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# for i in range(len(li)):
#     li[i]=list(li[i])
#     li[i].pop()
#     li[i].append(100)
#     li[i]=tuple(li[i])
# print(li)

#8 sum of digits of each number
# li=[10, 20, 4, 5, 'b', 70, 'a']
# sum=0
# for i in range(len(li)):
#     if type(li[i])==int:
#         while li[i]>0:
#             sum+=(li[i])%10
#             li[i]=li[i]//10
# print(sum)

