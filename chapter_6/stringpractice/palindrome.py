Name=input("enter a name")
Nam=Name
Namelen=len(Name)
rev=""
for i in range(Namelen,0,-1):
   lastchar=i-1
   revchar=Name[lastchar]
   rev+=revchar
print(rev)
if(rev==Nam):
    print("palindrome")
else:
    print("non palindrome")