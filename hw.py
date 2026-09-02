# 1 Write a program to create a file and write student details into it.
# with open("q1.txt","w") as f:
#     f.write("Name:Fazal Rahman \n Class:Python ")

# 2 Write a program to read and display the contents of a file
# with open("sample.txt","r") as f:
#     print(f.read())

# 3 Write a program to add new data to an existing file without removing the old data.
# with open("q1.txt","a") as f:
#     f.write("Class Started")

# 4 Write a program to create a new file and display an error message if the file already exists.
# f=open("q1.txt","x")

# 5 Write a program to write multiple lines into a file using a loop.
# f=open("sample1.txt","a")
# i=""
# while i!="0":
#     f.write(i+"\n")
#     i=input("Enter the line : ")

# 6 Write a program to read and display a file line by line using a loop.
# f=open("sample1.txt","r")
# for i in f:
#     print(i)

# 7 Write a program to count the number of lines in a file.
# f=open("sample1.txt","r")
# c=0
# for i in f:
#     c+=1
# print(c)

# 8 Write a program to display the current position of the file pointer before and after reading data.
# f=open("sample1.txt","r")
# print(f.tell())
# print(f.read(44))
# print(f.tell())

# 9 Write a program to move the file pointer to a specified position and read the remaining contents of the file.
# f=open("sample1.txt","r")
# f.seek(32)
# print(f.read())