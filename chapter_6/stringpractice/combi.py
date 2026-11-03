name=input("Enter name")
ch=name
print(ch)

for i in range(0,len(name)-1):
    oj=ch[1:]+ch[0]
    print(oj)
    ch=oj


