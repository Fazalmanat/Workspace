# import math
# print(math.pow(2,3))
# print(math.floor(10.999999999999999))
# print(math.ceil(10.000000000001))
# print(math.modf(54.9))
# print(math.factorial(5))
# print(math.sqrt(25))
# print(math.pi)

# import random
# list1=[1,2,3,4,5]
# # print(random.choice(list))
# # print(random.randint(1,100))
# random.shuffle(list1)
# while(list1!=[1,2,3,4,5]):
#     random.shuffle(list1)
#     print(list1)

import statistics
data=[1,2,4,5,6,3,1,4,6,8,3,3,5,9,0,8,2,3,1,5,7,7,4,4,2,9,0,1,3,4,7,1,1,2,2]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.mode(data))