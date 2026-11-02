digit=int(input("Enter the number: "))
digi=1
count=0
while(digi<=digit):
    count=count+1
    digi=digi//10
print("Digit", count)
