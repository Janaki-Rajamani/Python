lines=int(input("Enter number of rows:"))
x=1
for i in range(0,lines+1):
    for j in range(0,i):
        print(x, end=" ")
        x+=1
    print("")

