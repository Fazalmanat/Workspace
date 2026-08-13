# s="python"
# for i in range(len(s)+1):
#     for j in range(i):
#         print(s[j],end="")
#     print("\n")

# num= int(input("enter No of rows :"))
# num = num//2+1
# i=1
# while(i<num+1):
#     print("* "*i,end="")
#     print("    "*(num-i-1),end="")
    
#     if i!=num:
#         print(" ",end="")
#         print(" *"*i)
#     else:
#         print("* "*(i-1))
#     i+=1
# i-=1
# while(i>0):
#     i-=1
#     print("* "*i,end="")
#     print("    "*(num-i-1),end="")
#     print(" ",end="")
#     print(" *"*i)

num=int(input("Enter no of terms:"))
for i in range(1,num+1):
    if(i%2!=0):
        print("*"*i,end="")
    print("*"*i)