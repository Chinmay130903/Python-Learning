Binarynum=int(input("Enter binary number"))
userint=Binarynum
sum=0
n=1


while(userint>0):
        digit=userint%10
        num=digit*n
        sum=sum+num
        n=n+n
        userint=userint//10
print(sum)