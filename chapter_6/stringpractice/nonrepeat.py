name=input("Enter a string: ")
for i in range(0,len(name)):
    counti=name.count(name[i])
    
    if(counti==1):
        print(name[i])
        isfound=True
        break
    