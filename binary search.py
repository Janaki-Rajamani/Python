n=int(input("Enter number of elements:"))
sort_list=[]
print("enter numbers:")
for i in range(n):
    sort_list.append(int(input(str(i+1)+".")))

sort_list=sorted(sort_list)

print(sort_list)

    

loop=1
while loop==1:
    x=int(input("Enter number to search:"))
    start=0
    mid=n//2

    end=n-1
    found=0
    #if x==sort_list[mid]:
       # print("found at position:"+str(mid+1))
        
    if x<sort_list[mid]:
        end=mid
    else:
        start=mid

    while start<=end:
        if sort_list[start]==x:
            print("found at position:"+str(start+1))
            found=1
            break
        else:
            start+=1

    if found==0:
        print("not found")
    loop=int(input("Do you wish to continue(1 yes/0 no):"))        



