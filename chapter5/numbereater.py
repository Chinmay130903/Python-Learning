

userint=125

while(count!=1):
    newnumber=1
    count=0
    while(userint>=10):
        usert=userint%10
        newnumber*=usert
        userint=userint//10
        count+=1
    userint=newnumber
    
print(newnumber)


