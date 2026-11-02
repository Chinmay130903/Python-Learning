n=int(input("enter n"))

a=1
b=2
"""print(a,b,end="\n")"""
for i in range(5,n+1,2):
    isPrime=True
    count=0
    for j in range(3,i+1,2):
        if(i%j==0):
            isPrime=False
            count=count+1
    if(not isPrime and count==1):
        
        for p in range(1,n):
            print(i)