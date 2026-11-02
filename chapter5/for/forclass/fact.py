n=int(input("Enter a number for factorial"))
fact=1

for i in range(n,0,-1):
    fact=fact*i

print(fact)