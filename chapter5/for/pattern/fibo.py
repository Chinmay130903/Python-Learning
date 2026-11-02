num1=1
num2=0

  
for i in range(10):
        num3=num1+num2
        num1=num2
        num2=num3
        for j in range(num3):
            print("*",end="\t")
        print()