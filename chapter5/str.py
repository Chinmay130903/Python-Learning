i=input("Enter a string: ")
upper=0
lower=0
digit=0
sp=0
if(len(i)>=8):
    for char in i:
        if(char.isupper()):
            upper+=1
        elif(char.islower()):
            lower+=1
        elif(char.isdigit()):
            digit+=1
        else:
            sp+=1
    if(upper>0 and lower>0 and digit>0 and sp>0):
        print("Valid string")
    else:
        print("Invalid string")
else:
    print("String length should be at least 8 characters.")