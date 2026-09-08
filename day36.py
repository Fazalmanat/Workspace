# class employee:
#     id=1
#     name="fazal"
#     def display(self):
#         print(self.id,self.name)
# emp=employee()
# emp.display()

# class Employee:
#     def __init__(self, name1, id1):
#         self.id=id1
#         self.name=name1
#     def display(self):
#         print(self.id,self.name)
# emp=Employee("njan",1)
# emq=Employee("nee",2)
# emp.display()
# emq.display()

# class Student:
#     count=0
#     def __init__(self):
#         Student.count+=1
# s1=Student()
# s2=Student()
# s3=Student()
# print(Student.count)        

# class Employee:
#     def __init__(self):
#         print()
#     def display(self,name):
#         print("y :",name)
# emp=Employee()
# emp.display("b")

# class Employee:
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id
# s=Employee("john",23,1)
# print(getattr(s,'name'))
# setattr(s,'age',24)
# print(getattr(s,'age'))
# print(hasattr(s,'id'))
# delattr(s,'id')
# print(hasattr(s,'id'))