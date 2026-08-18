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

# import statistics
# data=[1,2,3,4,4,5,6,6,7,8,8,9]
# print(statistics.mean(data))
# print(statistics.median(data))
# print("%s"%(statistics.mode(data)))
# print(statistics.stdev(data))
# print(statistics.median_high(data))
# print(statistics.median_low(data))

#JSON
import json
# x='{"name":"Fazal","age":23,"address":"manat"}'
# y=json.loads(x)
# print(y)
# z=json.dumps(y)
# print(z)

# print(json.dumps({1:2,2:4,3:6}))
# print(json.dumps([1,2,3,4]))
# print(json.dumps((1,2)))
# print(json.dumps("1,/""2"))
# print(json.dumps(1))
# print(json.dumps(1.01))
# print(json.dumps(True))
# print(json.dumps(False))

x={
    'name':"fazal",
    'age':23,
    'course':"python",
    'place':"thalassery",
    'house':'manat',
    'lastDigits': '0166'
}
print(json.dumps(x,indent=2,separators=("","-->"),sort_keys=True))