n=int(input("Enter any number"))
sum=0
for i in range(n+1):
    if(i%3==0 or i%5==0):
        sum=sum+i
print(sum)