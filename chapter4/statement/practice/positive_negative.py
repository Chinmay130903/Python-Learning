age=int(input("Enter your age: "))
if age >= 18 and age <= 40:
    print("Plan A")

elif (age >= 41) and (age <= 60):
    print("Plan B")

elif age >= 61 :
    print("Plan C")
else:
    print("rejected")