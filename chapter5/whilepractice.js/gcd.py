a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=1
max=1
while(a>c):
    if(a%c==0 and b%c==0):
        ch=c
        c=c+1
        if(ch>max):
            max=ch
    else:
        c=c+1
print(max)