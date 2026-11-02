n=int(input("enter n"))
evencount=0
oddcount=0
devidebythree=0
for i in range(1,n+1):
    if(i%2==0):
        evencount+=1
    elif(i%2!=0):
        oddcount+=1
    if(i%3==0):
        devidebythree+=1
        print(i)
print("even count",evencount)
print("odd count",oddcount)
print("devide count",devidebythree)