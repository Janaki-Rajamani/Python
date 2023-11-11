line=input("Enter a string:")
alpha=[]
cnt=0
j=0 
  
while j<len(line):
        
    for k in range(len(alpha)):
        if alpha[k]==line[j]:
            cnt=1
            break
    
    if cnt==0:
        alpha.append(line[j])
    j+=1
    cnt=0

for i in range(len(alpha)):
    print(alpha[i],end="")
