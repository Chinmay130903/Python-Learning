name=input("Enter a string: ")
name1=input("Enter a string: ")
if(len(name)==len(name1)):
    for i in range(len(name)):
        for j in range(len(name1)):
            if(name[i]==name1[j]):
                break