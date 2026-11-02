n=int(input("x"))
sum=0
for i in range(1,n):
    divisor=(i+1)/2
    for j in range(1,divisor):
        if(i%j==0):
            sum+=j
    if(sum==n):
        print(i)

n=int(input("x"))

for i in range(1,n+1):
    sum=0
    
  
    for j in range(1,i):
        if(i%j==0):
            sum+=j
    if(sum==i):
        print(i)




