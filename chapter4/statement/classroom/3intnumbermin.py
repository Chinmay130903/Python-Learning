num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

min=num1
if(num2<min):
    min=num2
if(num3<min):
    min=num3 
print("The smallest number is ",min)