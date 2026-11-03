name=input("enter name")
isuppercount=0
islowercount=0
isdigitcount=0
isspecialcount=0
for i in range(0,len(name)):
    ch=name[i]
    if(ch.isupper()):
        isuppercount+=1
    elif(ch.islower()):
        islowercount+=1
    elif(ch.isdigit()):
        isdigitcount+=1
    else:
        isspecialcount+=1
print("upper case letters:",isuppercount)
print("lower case letters:",islowercount)
print("digits:",isdigitcount)
print("special characters:",isspecialcount)