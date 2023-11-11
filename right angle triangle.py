lines=int(input("Enter number of rows:"))

for i in range(0,lines+1):
    for j in range(0,i):
        print("*", end=" ")
    print()
