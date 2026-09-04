# try:
#     x=int(input("Enter No. 1 : "))
#     y=int(input("Enter No. 2 : "))
#     c=x/y
#     print(c)
# except:
#     print("Can't divide by Zero!")
# print("Finish")

# try:
#     x=int(input("Enter No. 1 : "))
#     y=int(input("Enter No. 2 : "))
#     c=x/y
#     print(c)
# except Exception as e:
#     print("Can't divide by Zero!")
#     print(e)
# else:
#     print("OR ELSE....")
# print("Finish")

# try:
#     x=int(input("Enter No. 1 : "))
#     y=int(input("Enter No. 2 : "))
#     c=x/y
#     print(c)
# except IOError as e1:
#     print("IOException ",e1)
# except ArithmeticError as e2:
#     print("Arithmetic Exception ",e2)
# else:
#     print("OR ELSE....")
# print("Finish")

# try:
#     x=int(input("Enter No. 1 : "))
#     y=int(input("Enter No. 2 : "))
#     c=x/y
#     print(c)
# except (IOError,ArithmeticError):
#     print("IOException ")

# else:
#     print("OR ELSE....")
# print("Finish")

try:
    x=int(input("Enter No. 1 : "))
    y=int(input("Enter No. 2 : "))
    if y==0:
        raise ArithmeticError("Zero...")

except Exception as e2:
    print(e2)


try:
    x=int(input("Enter No. 1 : "))
    y=int(input("Enter No. 2 : "))
    if y==0:
        raise ArithmeticError("Zero...")

except Exception as e2:
    print(e2)
