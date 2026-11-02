n=int(input("enter the number"))
nth = int(input(
    "Enter:\n"
    "1 for sum of digit\n"
    "2 for product of digit\n"
    "3 for reverse of digit\n"
    "4 for sum of even digit\n"
    "5 for sum of odd digit\n"
    "6 for multiplication of table\n"
    "7 for factorial of number\n"
    "--> "
))
sum=0
mul=1
rev=0
while(n>0):
    if(nth==1):
        while(n>=0):
            digit=n%10
            sum=sum+digit
            n=n//10
        print("sum of digit is",sum)
        n=0
    elif(nth==2):
        while(n>=0):
            digit=n%10
            mul=mul*digit
            n=n//10
        print("product of digit is ",mul)
        n=0
    elif((nth==3)):
        while(n>=0):
            digit=n%10
            rev=rev*10+digit
            n=n//10
        print("reverse of digit is ",rev)
        n=0
    elif(nth==4):
        while(n>=0):
            digit=n%10
            if(digit%2==0):
                sum=sum+digit
            n=n//10
        print("sum of even digit is ",sum)
    elif(nth==5):
        while(n>=0):
            digit=n%10
            if(digit%2!=0):
                sum=sum+digit
            n=n//10
        print("sum of odd digit is ",sum)
        n=0
    elif(nth==6):
        i=1
        while(i<=10):
            print(n,"*",i,"=",n*i)
            i=i+1
        n=0             
    elif(nth==7):
        fact=1
        while(n>=1):
            fact=fact*n
            n=n-1
        print("factorial of number is ",fact)
        n=0
    elif(nth==0):
        break
    else:
        print("invalid input")