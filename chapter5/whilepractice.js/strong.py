n=int(input("Enter the number: "))
ch=n
sum=0
fact=1
while(ch>0):
    digit=ch%10
    
    while(digit>=1):
        
        fact=fact*digit
        digit=digit-1
    sum=sum+fact
    fact=1


    ch=ch//10
print(sum)
if(sum==n):
    print("strong number")
else:
    print("not strong number")
