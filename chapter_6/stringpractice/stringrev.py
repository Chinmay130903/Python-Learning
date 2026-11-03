Name=input("enter a String ")
rev=""
namelength=len(Name)
for i in range(0,namelength):
    lastchar=len(Name)-1
    rev+=Name[lastchar]

    Name=Name[:lastchar]
print(rev)
