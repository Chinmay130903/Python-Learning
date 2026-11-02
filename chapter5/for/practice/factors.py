n=int(input("Enter n"))
count=0
for i in range(1,n):
    if(n%i==0):
        count+=1
        print(i)
print("count",count)
