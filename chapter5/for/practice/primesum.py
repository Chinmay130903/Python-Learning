n=int(input("enter number"))
count=0
for i in range(3,n):
    isprime=False
    for j in range(3,i+1):
        if(i%j!=0):
            count+=1
            isprime=True
        
    if(isprime and count==1):
        print(i)
    