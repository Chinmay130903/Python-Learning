n=input("enter a sigle charatcter")

if((n>='a' and n<='z') or (n>='A' and n<='Z')):
    if(n=='a' or n=='u' or n=='o' or n=='i' or n=='e' or n=='U' or n=='O' or n=='I' or n=='E' or n=='A' ):
        print("Vowel")
    else:
        print("consonent")  
else:
    print("Invalid input")