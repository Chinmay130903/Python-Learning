n=int(input("Enter the decimal number: "))
bin=""
userint=n
while(userint>=1):
    reminded=userint%2
    dividend=userint//2
    bin=bin+str(reminded)
    userint=dividend
print(bin)



"""binary number kadach ahe ter apan n number %2 mde modulo strore krto meant to number jer 2 ne divide kela ter kiti wachte ani tych divident means kitit ne zala yach 
// ya operator ne calclate krto """