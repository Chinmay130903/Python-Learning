name=input("enter name")
countconsonent=0
countvowel=0
for i in range(len(name)):
    is_vowel=name[i]=="a" or name[i]=="A" or name[i]=="e" or name[i]=="E" or name[i]=="i" or name[i]=="I" or name[i]=="o" or name[i]=="O" or name[i]=="U" or name[i]=="u"

    if(is_vowel):
        countvowel+=1
    elif(name[i]>='a' and name[i]<='z'  or name[i]>='A' and name[i]<='Z'):
        countconsonent+=1

  

print("Vowel",countvowel)
print("consonent",countconsonent)