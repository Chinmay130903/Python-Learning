userint=int(input("enter n"))
userint1=userint
largest = -1
secondlargest = -1
while(userint1>0):
    digit=userint1%10
    userint1=userint1//10
    if(digit>largest):
        secondlargest=largest
        largest=digit
    elif(digit<largest and digit>secondlargest and digit!=largest):
        secondlargest=digit
    
print(largest)
if(secondlargest>=0):
    print(secondlargest)
else:
    print("second large is 0   or number is of one digit or number is has consetutaive term")
