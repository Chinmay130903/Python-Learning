Number=int(input("Enter the number "))
UserInt=Number
max=1
secondmax=0
while(UserInt>=1):
    digit=UserInt%10
    if(digit>max):
        secondmax=max
        max=digit
    elif(digit>secondmax and max!=secondmax):
        secondmax=digit
    UserInt=UserInt//10
print(max)
print(secondmax)