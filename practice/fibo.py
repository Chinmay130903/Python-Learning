n=int(input("Enter the number of terms: "))
i=1
i2=1
p=1
print(i,i2,end="\t",sep="\t")
while(n>=p):
    i3=i+i2
    print(i3,end="\t")
    i=i2
    i2=i3
    p=p+1

