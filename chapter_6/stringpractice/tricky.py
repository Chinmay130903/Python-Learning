ch=input("enter name")
print(ch)
for j in range(0,len(ch)-1):
    str=ch[1:]+ch[0]
    print(str)
    ch=str