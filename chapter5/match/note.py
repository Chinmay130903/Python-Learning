amount=int(input("enter withdrawable amount"))
notefive=0
noteone=0
notetwo=0
if(amount%100!=0 or amount<=0 or amount>3600):
    print("Enter valid amount")
else:
    
    while(amount!=0):
        while(amount>=500):
            if(notefive<5):
                amount=amount-500
                notefive+=1
            else:
                 break
            
            
        while(amount>=200):
            if(notetwo<3):
                amount=amount-200
                notetwo+=1
            else:
                 break
        while(amount>=100):
            if(noteone<5):
                amount=amount-100
                noteone+=1
            else:
                 break
    
        if(amount==0):

            print("500 rs note is ",notefive)
            print("200 rs note is ",notetwo)
            print("100 rs note is ",noteone)

            print("500 remaining note",5-notefive)
            print("200 remaining note",3-notetwo)
            print("100 remaining note",5-noteone)
        else:
             print("insuffient notes")
        