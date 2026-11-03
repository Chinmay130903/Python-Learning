name=input("Enter a string")

for i in range(0,len(name)):
    count=0
    isprsent=False
    for j in range(i):
        if(name[i]==name[j]):
            count+=1
            
            
        else:
            print(name[i],"=",count)
            i=j
            isprsent=True
        
            break

            
    
