consumption_unit=float(input("Enter the unit of electricity consumed: "))
if(consumption_unit>0 and consumption_unit<=100):
    Total_bill=consumption_unit*5
elif(consumption_unit>100 and consumption_unit<=200):
    Total_bill=100*5+(consumption_unit-100)*7
elif(consumption_unit>200 and consumption_unit<=300):
    Total_bill=100*5+100*7+(consumption_unit-200)*10
elif(consumption_unit>300):
    Total_bill=100*5+100*7+100*10+(consumption_unit-300)*15

print("The total electricity bill is ",Total_bill)