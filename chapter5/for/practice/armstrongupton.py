n=int(input("x"))
num=n
isarmstrong=False




for i in range (1,num+1):

    number=i
    sum=0
    count=0
    cc=number
    while(cc>0):
      
        count+=1
        cc=cc//10

    armstrong=1
    while(number>0):
    
        digit=number%10
        number=number//10
        armstrong=1
        
        
        for k in range(count):
               
                armstrong*=digit
        sum=sum+armstrong
        
    if(sum==i):
        print(i)





