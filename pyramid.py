lines=int(input("Enter number of rows:"))
space=lines-1

for i in range(1,lines+1):
    for j in range(0,space):
        print(" ",end="")
    for k in range(0,i):
        print("*", end=" ")
    space=space-1
    print()
