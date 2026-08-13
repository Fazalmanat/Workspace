# common element check
# list1=[1,2,3,4,5]
# list2=[6,1,3,5,8]
# for i in list1:
#     if i in list2:
#         print(i)

#duplicate removal
# list1=[1,1,2,2,3,3,4,4]
# # list2=[]
# # for i in list1:
# #     if i not in list2:
# #         list2.append(i)
# # list1=list2
# for i in list1:
#     if list1.count(i)>1:
#         list1.remove(i)
# print(list1)
        
#reverse list without using reversec
#list1=input("enter the elements : ").split()
# for i in range(len(list1)//2):
#     temp=list1[i]
#     list1[i]=list1[-(i+1)]
#     list1[-(i+1)]=temp
# print(list1)

#count_odd_and even
# list1=input("Enter The Numbers : ").split()
# odd_count=0
# even_count=0
# for i in list1:
#     if int(i)%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
# print("No of odd numbers is ",odd_count," and no of even numbers is ",even_count)