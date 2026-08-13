# #list
# list1=["pen","pineapple","apple"]
# print(list1[0])
# print(list1)
# list1.append("applepen")
# list1.insert(1,"pineapplepen")
# print(list1)
# list1.remove("apple")
# list1.pop(1)
# print(list1)
# list2=["boom"]
# print(list1.remove("pen"))
# print(list1.append("penny"))
# print(list1.pop(1))
# print(list1.insert(1,"pennywise"))
# print(list1)
# for i in list1:
#     print(i)

#'difference of largest and smallest'
# list1=[5,-6,-7,-2,-4,-9,-5,-1,-1]
# print(max(list1)-min(list1))
# large=list1[0]
# small=list1[0]
# for i in list1:
#     if i>large:
#         large=i
#     if i<small:
#         small=i
# print(large-small)
# list1.sort( )
# print(list1[-1]-list1[0])

#Second Largest
list1=[1,2,3,5,4,5]
large=-float("inf")
small=float("inf")
slarge=-float("inf")
for i in list1:
    if i > slarge:
        if i >=large:
            if i!=large:
                slarge=large
            large=i
        else:
            slarge=i
    if i<small:
        small=i
print(large,slarge,small)