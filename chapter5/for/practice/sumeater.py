n=int(input("Enter sum"))
digit_sum=0
userint=n
if(userint<10):
    digit_sum=userint
else:
    while(userint>9):
        digit_sum=0
        useradd=userint
        
        while(useradd>0):
            digit=useradd%10
            useradd=useradd//10
            digit_sum+=digit
            
        userint=digit_sum
print(digit_sum)
    


    