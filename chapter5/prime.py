n=int(input("Enter a number"))
if(n<=1):
    print("not a prime")
elif(n==2):
    print("2")
else:
    for i in range(2,n+1):
        for j in range(2,i):
            if(i%j==0):
                
                break
        else:
            print(i)