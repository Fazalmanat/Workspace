# file1=open(r"C:\Users\manat\Desktop\SMEC\\sample.txt","r")
# print(file1.read())

# file1=open(r"C:\Users\manat\Desktop\SMEC\Workspace\sample.txt","w")
# file1.write(" Welcome to his world")
# file1.close()

# file1=open(r"C:\Users\manat\Desktop\SMEC\Workspace\sample.txt","a")
# file1.write(" Welcome to My world")
# file1.close()

# with open(r"C:\Users\manat\Desktop\SMEC\Workspace\sample.txt","r") as f:
#     print(f.read())

# with open(r"C:\Users\manat\Desktop\SMEC\Workspace\sample.txt","w") as f:
#     f.write("Rewritten")
    
with open(r"C:\Users\manat\Desktop\SMEC\Workspace\sample.txt","a") as f:
    f.write(" Appended")
