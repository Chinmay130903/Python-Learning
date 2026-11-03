name='1'
while(name!='0'):
    name=input("enter a string")
    rev=name[::-1]
    if(rev==name):
        print("palindrome")
    else:
        print("not palindrome")

    