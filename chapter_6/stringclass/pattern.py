name='1'
while(name!='0'):
    name=input("enter a string")

    for i in range(1,len(name)+1):
        for j in range(0,i):
            print(name[j],end=" ")
        print("")