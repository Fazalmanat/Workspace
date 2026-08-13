#num1 = int(input("Enter A Number:"))
#num2 = int(input("Enter Another Number:"))
#print("sum = ",num1+num2,"\ndifference = ",num1-num2,"\nproduct = ",num1*num2,"\nquotient = ",num1/num2,"\nfloor div = ",num1//num2,"\nremainder = ",num1%num2,"\nexponent = ",num1**num2)
#if num1>0:
#    print("positive")
#elif num1==0:
#    print("neutral")
#else:
#    print("negative")    
#if num1%2==0:
#    print("even")
#else:
#    print("odd")


#Electricity bill
unit = int(input("Enter the no of units:"))
if unit<100:
    bill= unit*5
elif unit<200:
    bill = 500 + (unit-100)*10
else:
    bill = 1500 + (unit-200)*15
print("your bill is ",bill)