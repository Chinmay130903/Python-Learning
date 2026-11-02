n=int(input("Enter the Number"))
ch=n
cho=0
lastdigit=ch%10
ch=ch//10
isTrue=True
while(ch>0):
    digit=ch%10
    if(not(digit<lastdigit)):
         isTrue=False
         print(digit)
         break
    else:
         ch=ch//10
if(isTrue):
     print("number is consecutive increment")
else:
     print("not increment")
            

