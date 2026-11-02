userint=int(input("enter the digit"))
n=userint
count=0
isfound=False
ispresentdouble=False
while(n>0):
    digit=n%10
    n=n//10
    oh=n

    while(oh>0):
        digit2=oh%10
    
        if(digit==digit2):
            isfound=True
            
        if(isfound):
            present=digit
            if(digit==present):
                ispresentdouble=True
                break
            else:
                count=count+1
        oh=oh//10

    

           
        
    
print(count)
       

  
