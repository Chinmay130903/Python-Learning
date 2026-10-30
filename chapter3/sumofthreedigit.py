digit=float(input("enter a 3 digit number"))
num1=digit%10
digit=digit//10
num2=digit%10
digit=digit//10
sum=num1+num2+digit
print("123sum of three digit ",sum)