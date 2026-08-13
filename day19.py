# my_set={1,2,3,4,1,3}
# print(my_set)
# my_set.add(6)
# print(my_set)
# my_set.remove(4)
# print(my_set)
# my_set.discard(3)
# print(my_set)
# my_set.pop()
# print(my_set)

# fr=frozenset({1,2,4,3,2})
# print(fr)
# fr=set(fr)
# fr.add(5)
# fr=frozenset(fr)
# print(fr)
# li=list(fr)
# li.append(6)
# print(li)
# fr=set(li)
# print(fr)

# my_dict={"apple":"red","banana":"yellow"}
# print(my_dict)
# my_dict["orange"]=["orange"]
# print(my_dict)
# my_dict["banana"]="greenish"
# print(my_dict)

#1 vowels and consonants
# vowels=["a","e","i","o","u"]
# s=input("Enter The string : ").lower()
# my_dict={"vowels":0,"cons":0}
# for i in s:
#     if i.isalpha():
#         if i in vowels:
#             my_dict["vowels"]+=1
#         else:
#             my_dict["cons"]+=1
# print(my_dict)

#2 common keys
# dict1 = {"a": 10, "b": 20, "c": 30, "d": 40}
# dict2 = {"b": 50, "c": 60, "e": 70}
# out=set(list(dict1))&set(list(dict2))
# print(out)   

#3 most frequent
# s=input("Enter the String : ")
# dict1={}
# large=-float("inf")
# for i in s:
#     if i in dict1:
#         dict1[i]+=1
#     else:
#         dict1[i]=1
#     if dict1[i]>large:
#         large=dict1[i]
# for i in dict1:
#     if dict1[i]==large:
#         print("most frequent letter is ",i)


#4 x,x*2 1 to n
# n=int(input("Enter The Number : "))
# dict1={x:x*2 for x in range(1,n+1)}
# print(dict1)

#5 group by first
# words = ['apple', 'ant', 'banana', 'ball', 'cat', 'car']
# dict1={}
# for i in words:
#     if i[0] not in dict1:
#         dict1[i[0]]=i
#     else:
#         dict1[i[0]]=[dict1[i[0]]]+[i]
# print(dict1)

#6 add common
d1={'a':100,'b':200,'c':500}
d2 = {'a':300,'b':200,'d':400}
for i in d2:
    if i in d1:
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]
print(d1)