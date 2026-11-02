n=int(input("Enter n"))
count=0
i=5

while(i<=n):
    j=3
    devisible=False
    while(j<i):
        if(i%j!=0):
            count=count+1
            j=j+1
        else:
             devisible=True
             break
            
    if(devisible):
        i=i+1
        continue
    if(count>1):
        print(i)
        i=i+1
    