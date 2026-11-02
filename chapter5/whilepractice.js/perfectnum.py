n=int(input("Enter the number of terms: "))
num=n//2
ch=1
sum=0
while(ch<=num):
    if(n%ch==0):
        print(ch)
        sum=sum+ch
        
    ch=ch+1
if(sum==n):
    print("perfect number")
else:
    print("not perfect number")