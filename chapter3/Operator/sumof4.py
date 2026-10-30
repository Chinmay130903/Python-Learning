digit=float(input("enter a four digit number"))
num1=digit%10
digit=digit//10
num2=digit%10
digit=digit//10
num3=digit%10
digit=digit//10

sum=num1+num2+num3+digit
print("sum of four digit ",sum)