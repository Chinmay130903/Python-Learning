a=float(input("enter a"))
b=float(input("enter b"))
c=float(input("enter c"))
if(a>b and a>c):
    print("a is largest")
elif(b>a and b>c):
    print("b is largest")
else:
    print("c is largest")
if(a>b ):
    print("b is  smallest")
else:
    print("a is smallest")
if(a==b or a==c or a==b or b==c ):
    print("any two numbers are equal")
if(a==b and a==c and b==c):
    print("all numbers are equal")
sum=a+b+c
if(sum%2!=0):
    print("sum of three numbers is odd")
