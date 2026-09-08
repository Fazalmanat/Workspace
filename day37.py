# class Animal:
#     def speak(self):
#         print("Animal Speaking!")
# class dog(Animal):
#     def bark(self):
#         print("Dog Barking!")
# d=dog()
# d.speak()
# d.bark()

# class Animal:
#     def speak(self):
#         print("Animal Speaking!")
# class dog(Animal):
#     def bark(self):
#         print("Dog Barking!")
# class pup(dog):
#     def follow(self):
#         print("Follows!")
# p=pup()
# p.speak()
# p.bark()
# p.follow()

# class lecture1:
#     def topic1(self):
#         print("first topic")
# class lecture2:
#     def topic2(self):
#         print("second topic")
# class lecture3(lecture1,lecture2):
#     def topic(self):
#         print("both again")
# l=lecture3()
# l.topic1()
# l.topic2()
# l.topic()

# class lecture1:
#     def topic1(self):
#         print("first topic")
# class lecture2:
#     def topic2(self):
#         print("second topic")
# class lecture3(lecture1,lecture2):
#     def topic(self):
#         print("both again")
# print(issubclass(lecture3,lecture1))
# print(issubclass(lecture2,lecture1))

# class lecture1:
#     def topic1(self):
#         print("first topic")
# class lecture2:
#     def topic2(self):
#         print("second topic")
# class lecture3(lecture1):
#     def topic(self):
#         print("both again")
# l=lecture3()
# print(isinstance(l,lecture3))
# print(isinstance(l,lecture1))
# print(isinstance(l,lecture2))