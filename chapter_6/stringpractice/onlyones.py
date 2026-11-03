name=input("Enter a String")
for i in range(0,len(name)):
    count=0
    isval=False
    for j in range(i,len(name)):
        if(name[i]==name[j]):
            count+=1
        if(count>1):
            isval=True
            
    if(not isval):
        print(name[i], end=" ")