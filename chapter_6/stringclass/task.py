name=input("enter name")
length=len(name)
spaceright=15-length//2
spaceleft=int(15-((length)/2))
print("*"*30)
print(" "*spaceleft,name," "*spaceright)
print('*'*30)