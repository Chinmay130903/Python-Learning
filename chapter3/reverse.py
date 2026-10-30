digit=int(input("enter a number"))
num=digit%10
digit=digit//10
num2=digit%10
digit=digit//10
reverse=num*100+num2*10+digit
print("reverse of number is ",reverse)