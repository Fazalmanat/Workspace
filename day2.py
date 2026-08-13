# num = int(input("Enter your number:"))
# if num >0:
#     print("positive")
#     if num>10:
#         print("greater than 10")
#     else:
#         print("less than 10")
# else:
#     print("negative")
# if num>0 and num>10:
#     print("hi")
# else:
#     print("bye")
# if num>0 or num>10:
#     print("why")
# else:
#     print("lie")

#Salary Calculator
# exp = int(input("Enter Your Experience In Years : "))
# salary = int(input("Enter Your Initial Salary : "))
# if exp <=3:
#     bonus=0
# elif exp<=5:
#     bonus = salary*5/100
# elif exp<=10:
#     bonus = salary*10/100
# else:
#     bonus = salary*15/100
# print("Your expected Salary is ",salary + bonus)

#Grade Calculator
# mark = int(input("Enter your Mark :"))
# if mark >=95:
#     grade="A+"
# elif mark >=90:
#     grade="A"
# elif mark >=85:
#     grade="B+"
# elif mark >=80:
#     grade="B"
# elif mark >=75:
#     grade="C+"
# elif mark >=70:
#     grade="C"
# elif mark >=65:
#     grade="D+"
# elif mark >=60:
#     grade="D"
# elif mark >=55:
#     grade="E+"
# elif mark >=50:
#     grade="E"
# else:
#     grade="F"
# if grade != "F":
#     print("You Have Passed!\nYour Grade is ",grade)
# else:
#     print("You have Failed! Your Grade is ",grade)

#Shape Parameters

# shape = input("Options:\n--1.Circle\n--2.Rectangle\n--3.Square\n Enter The Shape :")
# if shape=="1" or shape=="Circle" or shape=="circle":
#     radius=int(input("Enter the Radius: "))
#     print("The Area of Your Shape is ",(radius**2)*3.14,"\nThe Perimeter of your shape is ",radius*6.28 )
# elif shape=="2" or shape=="Rectangle" or shape=="rectangle":
#     length,breadth=int(input("Enter The length and breadth :"))
#     print("The Area of Your Shape is ",length*breadth,"\nThe Perimeter of your shape is ",2*(length+breadth) )
# elif shape=="3" or shape=="Square" or shape=="square":
#     side=int(input("Enter the length of a side:"))
#     print("The Area of Your Shape is ",side**2,"\nThe Perimeter of your shape is ",side*4 )
# else:
#     print("Invalid Input!")


#Prime Number
num=int(input("Enter your Number : "))
i=num//2
while(i>1):
    if num%i==0:
        i=0
        break
    else:
        i-=1
if i!=0 and num>1:
    print(num," is a prime number")
else:
    print(num," is not a prime number") 
